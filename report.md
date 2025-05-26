# Отчёт по работе №1: Практика Linux (VirtualBox)

**Литвин Георгий Дмитриевич**

<br>

**Дата рождения: 23.10.2002**


---

**Начинаем работу с создания одной ВМ на основе скачанного образа.** Дважды клонируем её. <br>
Далее настраиваем сетевые адаптеры по заданию:
- Вместо NAT - Сетевой мост
- Добавляем две внутренние подсети - `clientnet` и `servernet` <br> <br>

После настройки запускаем все три ВМ и конфигурируем hostname и user:
- `user=litvin_1, hostname=litvin_server (server)`
- `user=litvin_2, hostname=litvin_gateway (gateway)`
- `user=litvin_3, hostname=litvin_client (client)`

---

**Перейдем к настройке netplan конфигов.** <br>
Меняем конфигурационные файлы командой:
```shell
sudo nano /etc/netplan/00-installer-config.yaml
```
А также применяем новые сетевые настройки:
```shell
sudo netplan apply
```
Проверим полученный результат: <br>

![Netplan A](pics/netA.png)
![Netplan B](pics/netB.png)
![Netplan C](pics/netC.png)

---
**Linux A (server)**

<br>

В корневой папке создадим файл `app.py` с простым Flask приложением на три эндпоинта. <br>
Также напишем сервис для автозапуска приложения:

![Flask приложение и сервис для его запуска](pics/python.png)

---
**Linux B (gateway)**

<br>

Настроим `iptables` на ВМ-шлюзе для фильтрации пакетов по 5000 порту. <br>
Делаем это также через терминал командами по заданию. <br>
После изменения сохраняем конфигурацию через `iptables-persistent`. <br>
Проверим полученный результат: <br>

![ip_rules](pics/iptables.png)

---

**Тестирование**

<br>

Для проверки всей системы необходимо:
- Запустить `python3 app.py` на машине **А**
- Запустить `tcpdump` на машине **B**
- Начать отправлять `curl` запросы на машине **C**
Проверим полученный результат: <br>

![ВМ С](pics/python_check.png)

Также проверим логи `tcpdump` на машине **B**:

![get](pics/tcp_get.png)
![post](pics/tcp_post.png)
![put](pics/tcp_put.png)