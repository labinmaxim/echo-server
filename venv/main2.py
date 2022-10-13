import socket
from time import sleep

sock = socket.socket()
sock.setblocking(1)
print("Соединение с сервером")

PORT_DEFAULT = int(9090)
IP_DEFAULT = 'localhost'

user_port = input("Введите порт (e для значения по умолчанию):")
if user_port == "e":
    user_port = PORT_DEFAULT
    print(f"Установили порт {user_port} по умолчанию")

user_ip = input("Введите ip сервера (e для значения по умолчанию):")
if user_ip == "e":
    user_ip = IP_DEFAULT
    print(f"Установили ip-адресс {user_ip} по умолчанию")

sock.connect((user_ip, int(user_port)))

while True:
    data = sock.recv(1024)
    print(data.decode())
    msg = input("Enter ")
    if msg == "exit":
        break
    sock.send(msg.encode())

sock.close()
