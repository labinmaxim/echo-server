import socket
import time
import logging
import pickle
import threading

def prints(s):
	print("Простой эхо сервер")

def prog():
	logging.info(f"Подключение клиента {addr}")
	print(addr[0])
	a = {}
	print(a)
	if addr in a:
		mcg = "Привет"
		conn.send(mcg + a[addr[0]])
	else:
		mcg = "Введите имя"
		conn.send(mcg.encode())
		name = conn.recv(1024)
		a[addr[0]] = name

	msg = ''

	print("Прием данных")

	while True:
		data = conn.recv(1024)
		print(data.decode())
		if not data:
			break
		msg += data.decode()
		conn.send(data)

	logging.info(f"Отключение клиента")
	print(msg)
	conn.close()

sock = socket.socket()
print("Запуск сервера")
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.INFO)

PORT_DEFAULT = 9090
port = input("Введите порт enter для значения по умолчанию:")

if port == "enter":
    port = PORT_DEFAULT
    print(f"Установили порт {port} по умолчанию")
port = int(port)

while True:
	try:
		sock.bind(('', port))
		print(port)
		break
	except:
		port += 1

#размер очереди
sock.listen(5)

while True:
	conn, addr = sock.accept()
	potoc = threading.Thread(target=prog)
	potoc.start()


