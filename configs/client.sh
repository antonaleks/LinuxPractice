#! /bin/bash

IPADDR=192.168.9.101/24
SUBNET=192.168.17.0/24
GATEWAY=192.168.8.1

# IPADDR=192.168.9.100/24
# SUBNET=192.168.16.0/24
# GATEWAY=192.168.9.1

# s=IPADDR, p=SUBNET, g=GATEWAY
# Пример вызова ./client.sh -s 192.168.9.100/24 -p 192.168.16.0/24 -g 192.168.9.1

usage() { echo "Usage: $0 [-s] [-p]" 1>&2; exit 1; }

while getopts ":s:p:g:" o; do
    case "${o}" in
        s)
            s=${OPTARG}
            ;;
        p)
            p=${OPTARG}
            ;;
        g)
            g=${OPTARG}
            ;;
        *)
            ;;
    esac
done
shift $((OPTIND-1))

if [ -n "${s}" ]; then
    IPADDR=${s}
fi

if [ -n "${p}" ]; then
    SUBNET=${p}
fi

if [ -n "${g}" ]; then
    GATEWAY=${g}
fi

echo "IPADDR = ${IPADDR}"
echo "SUBNET = ${SUBNET}"
echo "GATEWAY = ${GATEWAY}"

echo "# Создаем новый адаптер и связываем его с eth0"
ip link add macvlan1 link eth0 type macvlan mode bridge

echo "# Добавляем ip address адаптеру"
ip address add dev macvlan1 $IPADDR

echo "# Включаем адаптер"
ip link set macvlan1 up

echo "# Проверяем что создалось"
ip a

echo "# Прописываем маршрут клиента к его подсети через шлюз gateway"
ip route add $SUBNET via $GATEWAY