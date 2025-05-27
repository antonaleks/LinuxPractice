# linux_hw
Отчет по практической работе с виртуальными машинами на ОС Linux Ubuntu 24.04.2


Работа начинается с создания и настройки виртуальных машин А, Б и С, где А - сервер, В - шлюз и С - клиент.
Ниже предствлены скрины настройки виртуальных машин и их состояние:
![lA](https://github.com/user-attachments/assets/f56d747e-8ed7-478a-8a48-09658b5529b7)
![lB](https://github.com/user-attachments/assets/3ca036d4-ab4f-49e7-8d5f-5e6af0e795ca)
![lC](https://github.com/user-attachments/assets/433c7a9b-32d3-4033-a36c-b89570f33eab)

---

На всех трех виртуальных машинах был изменён 'hostname' в соответствии с заданием в файле etc/hostname :
![etc_hostnameA (1)](https://github.com/user-attachments/assets/8baf5b48-20e2-43bb-bc03-26076d1739df)
![etc_hostnameB](https://github.com/user-attachments/assets/f145e03c-e9b9-4a26-a04b-46d7b1765f26)
![etc_hostnameC](https://github.com/user-attachments/assets/3b8d81fe-23e8-4f84-8ae9-372055d5f3d0)

После презагрузки машинам были присвоены новые 'hostname': <br>
ВМ А - shcerbakovaserver <br> ВМ Б - shcerbakovagateway <br> ВМ С - shcerbakovaclient

![hostnameA](https://github.com/user-attachments/assets/98458eb8-6b85-488d-b471-c26618bdafc6)
![hostnameC](https://github.com/user-attachments/assets/0885b811-0621-45bf-97ed-7c28fbca0cac)
![hostnameB](https://github.com/user-attachments/assets/c50691a5-7f0b-4536-9761-8c06824659c0)


---

Далее была произведена конфигурация виртуальных интерфейсов на всех трех виртуальных машинах:
![netplan_ipaA](https://github.com/user-attachments/assets/2f1838c0-cf51-4bbc-90f0-5f9117383459)
![netplan_ipaB](https://github.com/user-attachments/assets/d1851135-18b0-4f61-8ec7-c6af9631bea2)
![netplan_ipaC](https://github.com/user-attachments/assets/3d826db3-6c1d-41fa-bf64-a00a6e0eb795)

На ВМ А был для 'enp0s3' был выставлен автоматический ip-адрес, а для 'enp0s8' - "192.168.26.10/24" в соответствии с заданием; <br>
На ВМ Б был для 'enp0s3' был также выставлен автоматический ip-адрес, для 'enp0s8' - "192.168.26.1/24", а для enp0s9 - "192.168.6.1/24" в соответствии с заданием; <br>
На ВМ С был для 'enp0s3' выставлен автоматический ip-адрес, а для 'enp0s8' - "192.168.6.1/24" в соответствии с заданием;

---

Перейдем к рассмотрению процесса настраивания виртуальных машин по отдельности. 

Начнем с ВМ А. 

Создан http-сервер на порту 5000. Также были реализованы три эндпоинта (запрос /get, /post, /put). Ниже представлен результат настройки:

![flask_apppy](https://github.com/user-attachments/assets/512b78df-97f7-4326-ae00-37017c0fc1f7)

---

Рассмотрит ВМ Б. 

С помощью утилит ip route и iptables были настроены маршрут пакетов от ВМ A до ВМ C и была настроена фильтрация по порту 5000. 

Настройка маршрутов представлена ниже:

![nastroykaB](https://github.com/user-attachments/assets/86ae56c8-923b-489e-96cd-4ba0d9294faa)

---

Перейдем к ВМ С.

Ранее была представлена конфигурация ВМ С. А ниже представлены запросы, передаваемые через ВМ Б на ВМ А:

![get_post_put](https://github.com/user-attachments/assets/c62403b9-1683-4a16-bdfb-c558d645de3c)

Как можно заметить, ВМ С успешно получает фидбек от ВМ А.

---

Теперь рассмотрит фидбек, получаемый с ВМ А, и мониторинг с помощью 'tcpdump' по порту 5000, установленный на ВМ Б.

На скринах ниже представлено состояние ВМ А во время получения запросов с ВМ С:

![gpp_A](https://github.com/user-attachments/assets/28b301dd-f375-4133-a2e3-430737eca823)

Так же с помощью команды 'tcpdump' были получены логи передачи пакетов с ВМ С на ВМ А. Ниже представлены скрины.

Мониторинг запросов GET с ВМ С на ВМ А:
![logs_get](https://github.com/user-attachments/assets/de673c05-e077-4875-b30b-166d80d0e281)

Мониторинг запросов POST с ВМ С на ВМ А:

![logs_post](https://github.com/user-attachments/assets/6ad2142d-cf7e-4429-8c17-16ed08de83ee)

Мониторинг запросов PUT с ВМ С на ВМ А:

![logs_put](https://github.com/user-attachments/assets/4c9fc810-437c-4ce1-95af-fb1dbcb4825b)

---

По вышепредставленным скринам и описаниям происходящего можно сделать вывод, что все виртуальные машины были успешно настроены. Все три вида запросов с ВМ С на ВМ А через ВМ Б проходят успешно.

---
