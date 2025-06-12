# linux_hw
Отчет по практической работе с виртуальными машинами на ОС Linux Ubuntu 24.04.2


Работа начинается с создания и настройки виртуальных машин А, Б и С, где А - сервер, В - шлюз и С - клиент.
Ниже предствлены скрины настройки виртуальных машин и их состояние:
![lA](https://github.com/AlexKud2002/1Project/blob/main/lA.PNG)
![lB](https://github.com/AlexKud2002/1Project/blob/main/lB.PNG)
![lC](https://github.com/AlexKud2002/1Project/blob/main/lC.PNG)

---

После презагрузки машинам были присвоены новые 'hostname': <br>
ВМ А - sashaserver <br> ВМ Б - sashagateway <br> ВМ С - sashaclient

![hostnameA](https://github.com/AlexKud2002/1Project/blob/main/hostname.PNG)
![hostnameC](https://github.com/AlexKud2002/1Project/blob/main/hostnameB.PNG)
![hostnameB](https://github.com/AlexKud2002/1Project/blob/main/hostnameC.PNG)


---

Далее была произведена конфигурация виртуальных интерфейсов на всех трех виртуальных машинах:
![netplan_ipaA](https://github.com/AlexKud2002/1Project/blob/main/netplanipaA.PNG)
![netplan_ipaB](https://github.com/AlexKud2002/1Project/blob/main/netplanipaB.PNG)
![netplan_ipaC](https://github.com/AlexKud2002/1Project/blob/main/netplanipaC.PNG)

На ВМ А был для 'enp0s3' был выставлен автоматический ip-адрес, а для 'enp0s8' - "192.168.14.10/24" в соответствии с заданием; <br>
На ВМ Б был для 'enp0s3' был также выставлен автоматический ip-адрес, для 'enp0s8' - "192.168.14.1/24", а для enp0s9 - "192.168.3.1/24" в соответствии с заданием; <br>
На ВМ С был для 'enp0s3' выставлен автоматический ip-адрес, а для 'enp0s8' - "192.168.3.1/24" в соответствии с заданием;

---

Перейдем к рассмотрению процесса настраивания виртуальных машин по отдельности. 

Начнем с ВМ А. 

Создан http-сервер на порту 5000. Также были реализованы три эндпоинта (запрос /get, /post, /put). Ниже представлен результат настройки:

![flask_apppy](https://github.com/AlexKud2002/1Project/blob/main/A.PNG)

---

Рассмотрит ВМ Б. 

С помощью утилит ip route и iptables были настроены маршрут пакетов от ВМ A до ВМ C и была настроена фильтрация по порту 5000. 

Настройка маршрутов представлена ниже:

![nastroykaB](https://github.com/AlexKud2002/1Project/blob/main/B.jpg)

---

Перейдем к ВМ С.

Ранее была представлена конфигурация ВМ С. А ниже представлены запросы, передаваемые через ВМ Б на ВМ А:

![get_post_put](https://github.com/AlexKud2002/1Project/blob/main/g_p_p.jpg)

Как можно заметить, ВМ С успешно получает фидбек от ВМ А.

---

Теперь рассмотрит фидбек, получаемый с ВМ А, и мониторинг с помощью 'tcpdump' по порту 5000, установленный на ВМ Б.

На скринах ниже представлено состояние ВМ А во время получения запросов с ВМ С:

![gpp_A](https://github.com/AlexKud2002/1Project/blob/main/fask_app_py.jpg)

Так же с помощью команды 'tcpdump' были получены логи передачи пакетов с ВМ С на ВМ А. Ниже представлены скрины.

Мониторинг запросов GET с ВМ С на ВМ А:
![logs_get](https://github.com/AlexKud2002/1Project/blob/main/get.jpg)

Мониторинг запросов POST с ВМ С на ВМ А:

![logs_post](https://github.com/AlexKud2002/1Project/blob/main/post.jpg)

Мониторинг запросов PUT с ВМ С на ВМ А:

![logs_put](https://github.com/AlexKud2002/1Project/blob/main/put.jpg)

---

По вышепредставленным скринам и описаниям происходящего можно сделать вывод, что все виртуальные машины были успешно настроены. Все три вида запросов с ВМ С на ВМ А через ВМ Б проходят успешно.

---
