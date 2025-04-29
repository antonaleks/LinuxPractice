Отчет по практической работе с виртуальными машинами на ОС Linux Ubuntu 24.04.2

Работа начинается с создания и настройки виртуальных машин А, Б и С - сервера, шлюза и клиента соответственно.
Ниже предствлены скрины настройки виртуальных машин и их состояние:
![3 VM C](https://github.com/user-attachments/assets/aea185b9-502e-4e87-8646-738c90d8d457)
![2 VM B](https://github.com/user-attachments/assets/da9744cf-cc18-4d5b-8a47-9d854e0ad308)
![1 VM A](https://github.com/user-attachments/assets/e800ffc2-1e71-4821-8a16-a0d3fe862c1b)

---

На всех трех виртуальных машинах был изменён 'hostname' в соответствии с заданием:
![1 hostname and add user](https://github.com/user-attachments/assets/b6477e76-06de-4855-bf62-1acdab0898a2)
![2 hostname and add user](https://github.com/user-attachments/assets/342684de-5ae1-4ea0-a460-dcbc3a8738ae)
![3 hostname and add user](https://github.com/user-attachments/assets/70036e6b-164f-47d0-b8a6-ed1d698f2d61)

В итоге получилось присвоить виртуальным машинам новые 'hostname': <br>
ВМ А - asowslaserver <br> ВМ Б - asowslagateway <br> ВМ С - asowslaclient

А так же на всех трех виртуальных машинах успешно были добавлены новые пользователи 'not_asowsla' и присвоены пароли для авторизации

---

Далее была произведена конфигурация виртуальных интерфейсов на всех трех виртуальных машинах:
![1 configuration](https://github.com/user-attachments/assets/2185bfec-72ec-4fa8-87de-5b413970cd0f)
![2 configuration](https://github.com/user-attachments/assets/dd83cf2e-5b1b-45fd-a64d-f67c447ec4c0)
![3 configuration](https://github.com/user-attachments/assets/f7e060b5-3731-4e7a-80a8-c7a007a3dd23)

На ВМ А был для 'enp0s3' был выставлен автоматический айпи-адрес, а для 'enp0s8' - "192.168.31.10/24" в соответствии с заданием; <br>
На ВМ Б был для 'enp0s3' был также выставлен автоматический айпи-адрес, для 'enp0s8' - "192.168.31.1/24", а для enp0s9 - "192.168.3.1/24" в соответствии с заданием; <br>
На ВМ С был для 'enp0s3' выставлен автоматический айпи-адрес, а для 'enp0s8' - "192.168.3.1/24" в соответствии с заданием;

Все конфигурационные файлы также представлены отдельно в соответствующей папке 'configs' в репозиторие.

---

Перейдем к рассмотрению процесса настраивания виртуальных машин по отдельности. 

Начнем с ВМ А. 

Был http-сервер на порту 5000. Также были реализованы три эндпоинта (запрос /get, /post, /put). Ниже представлен результат настройки (скрин был сделал раньше, чем я поменял 'hostname' на тот, что в задании):
![1 app and webserver](https://github.com/user-attachments/assets/a4ab76d8-2cfb-4b20-907f-10d7a4ef2690)

Скрипты, описанные в 'app.py' и '/lib/systemd/system/web.server.service', представлены отдельно - в папках 'app' и 'configs' соответственно.

---

Рассмотрит ВМ Б. 

С помощью утилит ip route и iptables были настроены маршрут пакетов от ВМ A до ВМ C и была настроена фильтрация по порту 5000. 

Настройка маршрутов представлена ниже:
![2 iptables and routes](https://github.com/user-attachments/assets/3148be73-89ea-498b-8dd5-69410d437077)

---

Перейдем к ВМ С.

Ранее была представлена конфигурация ВМ С. А ниже представлены запросы, передаваемые через ВМ Б на ВМ А:
![3 requests](https://github.com/user-attachments/assets/1fd7407b-1e12-4e78-9ec3-2cdd15f43ebe)

Как можно заметить, ВМ С успешно получает фидбек от ВМ А.

---

Теперь рассмотрит фидбек, получаемый с ВМ А, и мониторинг с помощью 'tcpdump' по порту 5000, установленный на ВМ Б.

На скринах ниже представлено состояние ВМ А во время получения запросов с ВМ С:
![1 responses](https://github.com/user-attachments/assets/76eb76bd-7aff-42c6-9707-b41139d26c4d)

Так же с помощью команды 'tcpdump' были получены логи передачи пакетов с ВМ С на ВМ А. Ниже представлены скрины.

Мониторинг запросов GET с ВМ С на ВМ А:
![2 tcpdump GET](https://github.com/user-attachments/assets/ac0935ff-3e67-401e-9c00-0affb7b21197)

Мониторинг запросов POST с ВМ С на ВМ А:
![2 tcpdump POST](https://github.com/user-attachments/assets/ba3f4544-b076-4fda-8faf-062331758438)

Мониторинг запросов PUT с ВМ С на ВМ А:
![2 tcpdump PUT](https://github.com/user-attachments/assets/9beca983-1933-43f9-b6ef-4238be1f7885)

---

По вышепредставленным скринам и описаниям происходящего можно сделать вывод, что все виртуальные машины были успешно настроены. Все три вида запросов с ВМ С на ВМ А через ВМ Б проходят успешно.

---
