# Отчёт по лабораторной работе: Настройка сети между виртуальными машинами

## Цель работы
Настроить связь между тремя виртуальными машинами (A, B, C) с маршрутизацией через шлюз (Машина B) и развернуть веб-сервер.

## Выполненные шаги

### 1. Настройка сети
- **Машина A (Сервер)**
  - IP: 192.168.25.10/24
  - Интерфейс: enp0s8
  ```yaml
  # configs/machine_A_netplan.yaml
  network:
    version: 2
    ethernets:
      enp0s8:
        addresses: [192.168.25.10/24]
  ```

- **Машина B (Шлюз)**
  - IP: 192.168.25.1/24 (enp0s8) и 192.168.3.1/24 (enp0s9)
  - Включен IP-форвардинг
  ```bash
  echo 1 > /proc/sys/net/ipv4/ip_forward
  ```

### 2. Настройка маршрутов
```bash
# На Машине A:
sudo ip route add 192.168.3.0/24 via 192.168.25.1

# На Машине C:
sudo ip route add 192.168.25.0/24 via 192.168.3.1
```

### 3. Развертывание веб-сервера
- Запущен Flask-сервер на Машине A:
```python
# application/app.py
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Machine A"

app.run(host='192.168.25.10', port=5000)
```

## Результаты
- Успешный ping между всеми машинами
- Доступ к веб-серверу с Машины C:
  ```bash
  curl http://192.168.25.10:5000
  > Hello from Machine A
  ```