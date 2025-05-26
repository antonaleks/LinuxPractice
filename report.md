# Отчёт по работе №1: Практика Linux (VirtualBox)

<br>

**Паутов Владислав Николаевич**
**Дата рождения: 28.06.2002**

<br>

## 1. Создание ВМ
Начинаем работу с создания одной ВМ на основе скачанного образа. Дважды клонируем её. <br>
Далее настраиваем сетевые адаптеры по заданию:
- Вместо NAT - Сетевой мост
- Добавляем две внутренние подсети - `clientnet` и `servernet` <br> <br>

После настройки запускаем все три ВМ и конфигурируем hostname и user:
- `user=pautov_1, hostname=pautov_server (server)`
- `user=pautov_2, hostname=pautov_gateway (gateway)`
- `user=pautov_3, hostname=pautov_client (client)`

## 2. Конфигурация netplan
Перейдем к настройке netplan конфигов. <br>
Меняем конфигурационные файлы командой:
```shell
sudo nano /etc/netplan/00-installer-config.yaml
```
А также применяем новые сетевые настройки:
```shell
sudo netplan apply
```
Проверим полученный результат: <br>

![Netplan A](pictures/netplanA.png)
![Netplan B](pictures/netplanB.png)
![Netplan C](pictures/netplanC.png)

## 3. Индивидуальная настройка ВМ
### Linux A (server)
В корневой папке создадим файл `app.py` с простым Flask приложением на три эндпоинта. <br>
Также напишем сервис для автозапуска приложения:

![Flask приложение и сервис для его запуска](pictures/pythonA.png)

### Linux B (gateway)
Настроим `iptables` на ВМ-шлюзе для фильтрации пакетов по 5000 порту. <br>
Делаем это также через терминал командами по заданию. <br>
После изменения сохраняем конфигурацию через `iptables-persistent`. <br>
Проверим полученный результат: <br>

![ip_rules](pictures/ip_rules.png)

## 4. Тестирование всей системы
Для проверки всей системы необходимо:
- Запустить `python3 app.py` на машине **А**
- Запустить `tcpdump` на машине **B**
- Начать отправлять `curl` запросы на машине **C**
Проверим полученный результат: <br>

![ВМ С](pictures/python_check.png)

Также проверим логи `tcpdump` на машине **B**:

![get](pictures/tcp_get.png)
![post](pictures/tcp_post.png)
![put](pictures/tcp_put.png)