#Linux #github 

https://github.com/antonaleks/LinuxPractice

# Введение

Данная практика посвещена базовым принципам администрирования Linux. Для выполнения практики необходимо развернуть 3 виртуальные машины Linux.

Как пример, можно использовать Virtual Box + Ubuntu Server 20.04.

# Задание

Для выполнения данного задания необходимо:

1. Развернуть три виртуальные машины Linux, согласно схеме ниже

[![info](https://github.com/antonaleks/LinuxPractice/raw/main/Linux%20Practice.png)](https://github.com/antonaleks/LinuxPractice/blob/main/Linux%20Practice.png)

2. Linux A
- [x] Сконфигурировать Hostname следующим образом: <your_surname>_server (пропустить если делаете через Play with docker)
- [x] Создать пользователя <your_surname>_1 (пропустить если делаете через Play with docker)
- [x] Сконфигурировать виртуальный интерфейс со следующим ip адресом: 192.168.<день рождения>.10/24
- [x] Развернуть Http сервер на виртуальной машине на порту 5000. Необходимо реализовать минимум три эндпоинта (запрос /get, /post, /put)
2. Linux B
- [x] Сконфигурировать Hostname следующим образом: <your_surname>_gateway (пропустить если делаете через Play with docker)
- [x] Создать пользователя <your_surname>_2 (пропустить если делаете через Play with docker)
- [x] Сконфигурировать 2 виртуальных интерфейс со следующими ip адресом: 192.168.<день рождения>.1/24, 192.168.<месяц рождения>.10/24
- [x] С помощью утилит ip route и iptables настроить маршрут пакетов от Linux A до C. Должны быть запрещены все пакеты, кроме http пакетов через порт 5000 (маршруты обязательно, файрвол опционально)
- [x] Запустить программу tcpdump с фильтрацией по портам 5000
2. Linux C
- [x] Сконфигурировать Hostname следующим образом: <your_surname>_client (пропустить если делаете через Play with docker)
- [x] Создать пользователя <your_surname>_3 (пропустить если делаете через Play with docker)
- [x] Сконфигурировать виртуальный интерфейс со следующим ip адресом: 192.168.<месяц рождения>.100/24
- [x] С помощью команды curl на машине C послать 3 запроса на машину А в http сервер (/get, /post, /put)
- [x] При перезагрузки системы все сервисы и сетевая архитектура должны также функционировать (сохранить свои настройки)
- [x] Сделать скриншоты всех этапов задания
- [x] Оформить отчет в виде Markdown файла. Приложить конфигурационные файлы в репозиторий
- [x] Для play with docker также нужно написать bash скрипты для воспроизведения на новых вм

Репозиторий оформить следующим образом:

- application - исходный код http сервера
- configs - конфигурационные файлы сетевых настроек виртуальных машин
- report.md - Отчет markdown

P.S. Если не получилось использовать разные утилиты для настройки сети, используйте netplan Смотрите [мануал](https://github.com/antonaleks/LinuxPractice/blob/main/guide/Manual.md) - там информация для virtual box и Play with docker

# Отчет по практической работе: Базовые принципы администрирования Linux
____________
**Цель работы:** Настройка трех виртуальных машин Linux (сервер, шлюз и клиент), конфигурация сети между ними, настройка маршрутизации с фильтрацией трафика и развертывание просто веб-сервера.

**Инструменты:** VirtualBox, Ubuntu Server 20.04.06 LTS.

Данные:
- Фамиля: Абышев
- День рождения: 21
- Месяц рождени: май (5)

# Глава 1. Подготовка виртуальных машин
___________
### Linux_A
	Your name: Linux_A
	Your server's name: orange_server
	Pick a username: orange

![screenshots](screenshots/Pasted%20image%2020260309042351.png)

### Linux_B
	Your name: Linux_B
	Your server's name: orange_server_2
	Pick a username: orange_2

![screenshots](screenshots/Pasted%20image%2020260310021629.png)

### Linux_C
	Your name: Linux_C
	Your server's name: orange_server_3
	Pick a username: orange_3

![screenshots](screenshots/Pasted%20image%2020260310033946.png)

# Глава 2. Настройка Linux A (сервер)
_____
2.1. Имя хоста и пользователь
- Hostname: orange_server
- Пользователь: orange
2.2. Настройка сети
	Сетевые адаптеры в VirtualBox:
	- Адаптер 1: Сетевой мост (для доступа)
	- Адаптер 2: Внутренняя сеть

Сгенерируем ключ:

![screenshot](screenshots/Pasted%20image%2020260310094948.png)

Подставим IP:

![screenshot](screenshots/Pasted%20image%2020260310095415.png)

Конфигурация Netplan (/etc/netplan/00-installer-config.yaml):

![screenshot](screenshots/Pasted%20image%2020260311073021.png)

Проверка IP - адресов после применения netplan:

![screenshot](screenshots/Pasted%20image%2020260311073036.png)

2.3. Настройка веб-сервера (Flask):
	Установим flask: 

![screenshot](screenshots/Pasted%20image%2020260309064644.png)

Завершена:

![screenshot](screenshots/Pasted%20image%2020260309064712.png)

Создадим директорию для http_server:

![screenshot](screenshots/Pasted%20image%2020260309065357.png)

Проверим текущую директорию с помощью команды pwd и создадим файл orange_5000.py

![screenshot](screenshots/Pasted%20image%2020260309065830.png)

![screenshot](screenshots/Pasted%20image%2020260309074957.png)

Проверим путь к файлу flask с помощью команды which flask: 

![screenshot](screenshots/Pasted%20image%2020260309081201.png)

Создадим systemd unit файл, который будет запускать сервер автоматически при старте системы:

![screenshots](screenshots/Pasted%20image%2020260310064843.png)

Включим и запустим:

![screenshots](screenshots/Pasted%20image%2020260309081451.png)

Результат:

![screenshots](screenshots/Pasted%20image%2020260309091031.png)

# Глава 3. Настройка Linux B (шлюз)
 
3.1. Имя хоста и пользователь
- Hostname: orange_server_2
- Пользователь: orange_2
3.2. Настройка сети:
	Сетевые адаптеры в VirtualBox:
	- Адаптер 1: Внутренняя сеть
	- Адаптер 2: Внутренняя сеть
	- Адаптер 3: Сетевой мост (для доступа)
	
Отредактируем файл net-plan:

![screenshot](screenshots/Pasted%20image%2020260310022655.png)
![screenshot](screenshots/Pasted%20image%2020260310023114.png)

Внесенные изменения с помощью команды netplan apply:

![screenshot](screenshots/Pasted%20image%2020260311072700.png)

Посмотрим изменения через ip a:

![screenshots](screenshots/Pasted%20image%2020260311072723.png)

3.3. Настройка маршрутизации и файрвола:
Включение IP Forwaarding:

![screenshots](screenshots/Pasted%20image%2020260310024954.png)

![screenshots](screenshots/Pasted%20image%2020260310025033.png)

По умолчанию запрещаем весь  пересылаемый через сервер трафик:

![screenshots](screenshots/Pasted%20image%2020260310025717.png)

Чтобы разрешить переброс только конкретных пакетов по конкретному порту, следует настроить маршрут. Проверим внесенные правила с помощью iptables -L:

![screenshots](screenshots/Pasted%20image%2020260311071654.png)

Сохраним внесенные изменения:

![screenshots](screenshots/Pasted%20image%2020260310032151.png)
![screenshots](screenshots/Pasted%20image%2020260311072937.png)

# Глава 4. Настройка Linux C
4.1. Имя хоста и пользователь
- Hostname: orange_server_3
- Пользователь: orange_3
4.2. Настройка сети:
	Сетевые адаптеры в VirtualBox:
	- Адаптер 1: Внутренняя сеть
	- Адаптер 2: Сетевой мост (для доступа)
	
Проверим текущие интерфейсы:

![screenshots](screenshots/Pasted%20image%2020260311072412.png)

Конфигурация Netplan (/etc/netplan/00-installer-config.yaml

![screenshots](screenshots/Pasted%20image%2020260311072444.png)

Проверка IP- адрессов:

![screenshots](screenshots/Pasted%20image%2020260310070423.png)

Установка curl:

![screenshots](screenshots/Pasted%20image%2020260310044609.png)

# Глава 5. Тестирование

## 5.1. Запуска tcpdump на шлюзе (Linux_B):

![screenshots](screenshots/Pasted%20image%2020260310070638.png)

## 5.2. Отправка запросов с клиента Linux_C на сервер Linux_A
С клиента (С) выполнены команды curl к серверу А:
- GET:

![screenshots](screenshots/Pasted%20image%2020260311072037.png)
![screenshots](screenshots/Pasted%20image%2020260311072128.png)

- POST:

![screenshots](screenshots/Pasted%20image%2020260311072157.png)
![screenshots](screenshots/Pasted%20image%2020260311072211.png)

- PUT:
 
![screenshots](screenshots/Pasted%20image%2020260311072249.png)
![screenshots](screenshots/Pasted%20image%2020260311072240.png)
 
 
## 5.4. Проверка блокировки другого трафика
Попытка выполнить ping с клиента C на сервер А была неуспешной (пакеты блокируются шлюзом B):

![screenshots](screenshots/Pasted%20image%2020260310071444.png)

# Глава 6. Проверка сохранения  настроек после перезагрузки
Все три виртуальные машины были перезагружены с помощью команды sudo reboot. После перезагрузки выполнены следующие проверки:
- IP Forwarding на Linux B активен:

	 ![screenshots](screenshots/Pasted%20image%2020260310072821.png)
  
- Правила iptables на Linux_B загружены:
 
	![screenshotss](screenshots/Pasted%20image%2020260311071654.png)

- Веб-сервер на Linux_A запущен:

	![screenshots](screenshots/Pasted%20image%2020260310073104.png)

- Тестовый запрос с Linux_C на Linux_A:
 
	![screenshots](screenshots/Pasted%20image%2020260311071532.png)
	![screenshots](screenshots/Pasted%20image%2020260310073243.png)
	![screenshots](screenshots/Pasted%20image%2020260310073459.png)

# Глава 7. Вывод
В ходе выполнения практической работы №1 "Базовые принципы администрирования Linux" была успешна настроена сетевая инфраструктура из трех виртуальных машин Linux. Настроен IP - адрес для сервера (А) и клиента (С), а также два статических IP для шлюза (B). С помощью iptables на шлюзе настроена маршрутизация и фильтрация трафика, разрешающая только HTTP - запросы на порт 5000 от клиента к серверу. Веб - сервер FLask был развернут на сервере и настроен для автозапуска с помощью systemd. Все настройки сохраняются после перезагрузки системы.   
# Используемая литература:

1. https://1cloud.ru/help/linux/change_ip_in_ubuntu_20 - # Замена IP в Ubuntu 20.04 с помощью net-tools.
2. https://habr.com/ru/articles/783574/ - # Flask для начинающих
3. https://flask.palletsprojects.com/en/stable/quickstart/
4. https://habr.com/ru/companies/slurm/articles/255845/ - # Systemd за пять минут
5. https://tokmakov.msk.ru/blog/item/494
6. https://timeweb.cloud/docs/unix-guides/iptables-setup 
7. https://habr.com/ru/articles/747616/ - # Введение в Iptables
8. https://pc.ru/articles/poluchenie-root-prav-pri-rabote-v-winscp - # Получение root прав при работе в WinSCP
