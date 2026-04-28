# ОТЧЕТ ПО ПРАКТИКЕ LINUX ШЕФЛЕР
### Общая информация
Дата рождения: 16  
Месяц рождения: 3  
ip - адреса машин на сетевом мосту:
    LinuxA: 192.168.0.113
    LinuxB: 192.168.0.114
    LinuxC: 192.168.0.104
## Linux A
### Информация о машине:
Имя хоста: shefler_server  
Имя пользователя shefler_1  
Пароль: shefler_1  
1. Настроим сетевые интерфейсы машины: Сетевой мост и Внутреннюю сеть (servernet):  
    
    ![Сетевой мост LinuxA](screenshots/LinuxA_screen/1.1.png)  
    ![Внутренняя сеть LinuxA](screenshots/LinuxA_screen/1.2.png)  
2. Пробуем пинговать машину с хоста:  
    
    ![Пинг LinuxA с хоста](screenshots/LinuxA_screen/3.png)  
3. Генерируем и копируем ключ для доступа по ssh, что затем поможет подключаться соответствующим образом с хоста:  

    ![Генерация и копирование SSH-ключа](screenshots/LinuxA_screen/4.png)  
4. Настраиваем сеть открыв конфигурационный файл 00-installer-config.yaml с помощью sudo nano /etc/netplan/00-installer-config.yaml:  

    ![Конфигурационный файл LinuxA](screenshots/LinuxA_screen/5_попытка.png)  
5. Примерим настройки и проверим их с помощью sudo netplan apply и ip addr:  

    ![Проверка конфигурации LinuxA](screenshots/LinuxA_screen/5-6.png)  
6. Настроим веб-сервер при помощи python flask. Для этого сначала проведем установку:  

    ![Установка flask1](screenshots/LinuxA_screen/install_flask1.png)  
    ![Установка flask1](screenshots/LinuxA_screen/install_flask2.png)  
7. Создадим директорию для сервера, а в ней файл shefler_5000.py:  

    ![Создание shefler_5000.py](screenshots/LinuxA_screen/making_shefler_5000.py.png)  
8. Запишем в файл следующее содержание:  

    ![Создание shefler_5000.py](screenshots/LinuxA_screen/shefler_5000.py.png)  
9. Создадим systemd unit файл для автоматического запуска сервера:  

    ![Создание systemd unit файла](screenshots/LinuxA_screen/http_shefler_server_service.service.png)  
10. Запустим и посмотрим на результат:

    ![Запуск сервера](screenshots/LinuxA_screen/start_service.png)  
    ![Результат запуска](screenshots/LinuxA_screen/service_working.png)  
## Linux B
### Информация о машине:
Имя хоста: shefler_gateway  
Имя пользователя shefler_2  
Пароль: shefler_2  
1. Настроим сетевые интерфейсы машины: Сетевой мост и Внутреннюю сеть (servernet и clientnet):  
    
    ![Сетевой мост LinuxB](screenshots/LinuxB_screen/1.1.png)  
    ![Внутренняя сеть LinuxB (servernet)](screenshots/LinuxB_screen/1.2.png)  
    ![Внутренняя сеть LinuxB (clientnet)](screenshots/LinuxB_screen/1.3.png)  
2. Убеждаемся, что один из интерфейсов подключен к той же подсети, что и хост. Запоминаем ip адрес:  

    ![Ip - адреса](screenshots/LinuxB_screen/2.png)  
3. Генерируем и копируем ключ для доступа по ssh, что затем поможет подключаться соответствующим образом с хоста:  

    ![Генерация и копирование SSH-ключа](screenshots/LinuxB_screen/3.png)  
4. Настраиваем сеть открыв конфигурационный файл 00-installer-config.yaml с помощью sudo nano /etc/netplan/00-installer-config.yaml:  

    ![Конфигурационный файл LinuxB](screenshots/LinuxB_screen/4.png)  
5. Применим настройки и проверим их с помощью sudo netplan apply и ip addr:  

    ![Проверка конфигурации LinuxB](screenshots/LinuxB_screen/6.png)  
6. Включим IP Forwarding c помощью редактирования sysctl.conf, а затем проверим:  

    ![Редактирование файла sysctl.conf](screenshots/LinuxB_screen/Включение_ip_forvarding.png)  
    ![Проверка результата](screenshots/LinuxB_screen/Включение_ip_forvarding_2.png)  
7. Для настройки маршрута внесем правила в ip tables и проведем проверку, а также сохраним в файлы 15-ip4tables и 25-ip6tables:  

    ![Проверка результата](screenshots/LinuxB_screen/маршруты.png)  
## Linux C
### Информация о машине:
Имя хоста: shefler_client  
Имя пользователя shefler_3  
Пароль: shefler_3  
1. Настроим сетевые интерфейсы машины: Сетевой мост и Внутреннюю сеть (clientnet):  
    
    ![Сетевой мост LinuxC](screenshots/LinuxC_screen/1.1.png)  
    ![Внутренняя сеть LinuxC](screenshots/LinuxC_screen/1.2.png)  
2. Генерируем и копируем ключ для доступа по ssh, что затем поможет подключаться соответствующим образом с хоста:  

    ![Генерация и копирование SSH-ключа](screenshots/LinuxC_screen/3.png)  
3. Настраиваем сеть открыв конфигурационный файл 00-installer-config.yaml с помощью sudo nano /etc/netplan/00-installer-config.yaml:  

    ![Конфигурационный файл LinuxC](screenshots/LinuxC_screen/4.png)  
4. Примерим настройки и проверим их с помощью sudo netplan apply и ip addr:  

    ![Проверка конфигурации LinuxC](screenshots/LinuxC_screen/6.png)  
5. Для копирования файлов с виртуальных машин на хост используется WinSCP:  

    ![WinSCP](screenshots/LinuxC_screen/WinSCP.png)  
6. Установим curl:  

    ![Установка curl на клиент](screenshots/LinuxC_screen/Загрузка_curl.png)  
## Тестирование
1. Запустим утилиту tcpdump на LinuxB:  

    ![Запуск утилиты](screenshots/Testing_screen/LinuxB_запуск_tcpdump.png)  
2. Отправим ряд curl-запросов с клиента (LinuxC) на cервер LinuxA для проверки:  
    2.1. GET:  

    ![Get1](screenshots/Testing_screen/Get1.png)  
    ![Get2](screenshots/Testing_screen/Get2.png)  
    2.2. POST:  

    ![Post1](screenshots/Testing_screen/Post1.png)  
    ![Post2](screenshots/Testing_screen/Post2.png)  
    2.3. PUT:  

    ![Put1](screenshots/Testing_screen/Put1.png)  
    ![Put2](screenshots/Testing_screen/Put2.png)  
    При прослушивании трафика через tcpdump видно последовательную смену TCP-флагов (SYN → SYN-ACK → ACK → PSH/ACK), что подтверждает успешное установление соединения и обмен данными между клиентом и сервером.  
3. Проверим блокировку трафику шлюзом попытавшись произвести пинг сервера клиентом:  

    ![Проверка блокировки трафика](screenshots/Testing_screen/проверка_блокировки.png)  
## Тестирование после перезагрузки
Послее перезагрузки всех машин проверим, что их настройки сохранены  

1. Проверим активен ли IP Forwarding, а также iptables на шлюзе:

    ![Проверка IP Forwarding](screenshots/Reboot_screen/1.png)  
2. Проверка того, запущен ли веб-сервер:
    ![Проверка веб-сервер](screenshots/Reboot_screen/2.png)  
3. Произведем тестовый запрос с клиента на сервер:  
    ![Проверка curl1](screenshots/Reboot_screen/3.png)  
    ![Проверка curl2](screenshots/Reboot_screen/4.png)  

Таким образом, после перезагрузки все настройки сохраняются.
## Заключение  

В ходе выполнения практической работы были развернуты три виртуальные машины Linux (Server, Gateway, Client) и настроена их сетевая связность в соответствии с заданной схемой.

На машине Linux A был развернут HTTP-сервер на базе Flask, реализующий обработку запросов GET, POST и PUT на порту 5000. Для обеспечения автоматического запуска сервиса при загрузке системы был создан systemd unit.

На машине Linux B была выполнена настройка маршрутизации между подсетями с использованием IP forwarding и правил iptables, обеспечивающих передачу только HTTP-трафика через порт 5000. Дополнительно была настроена фильтрация и мониторинг трафика с использованием tcpdump.

На машине Linux C была выполнена настройка сетевых интерфейсов и проверка взаимодействия с сервером с помощью утилиты curl.

В результате тестирования подтверждена корректная работа сетевой архитектуры: клиент успешно отправляет HTTP-запросы к серверу через шлюз, а весь трафик проходит через настроенные правила маршрутизации. Также установлено, что после перезагрузки системы все конфигурации сохраняются и функционируют корректно.