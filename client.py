import socket
import threading

# создание сокета
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# данные сервера
server = '127.0.0.1', 5050

line = input("Введите ваш логин: ")

# подпрограмма отправки сообщений
def post():
    # "глухой" цикл – отправка информации программой
    while True:
        # Ввод сообщения пользователем
        print("Вы можете написать сообщение другим пользователям:")
        data = input()
        # отправляем сообщение на сервер
        sock.sendto(data.encode('utf-8'), server)

while True:
    # отправляем данные на сервер
    sock.sendto(('login ' + line).encode('utf-8'), server)
    # получаем ответ
    data = sock.recv(1024).decode('utf-8')
    # Выводим в консоль
    print(data)
    if data.startswith('Добро пожаловать в чат'):
        # Запускаем поток отправки сообщений
        threading.Thread(target=post).start()
        # Прерываем цикл ввода данных
        break
    else:
        # Запрашиваем новую команду
        line = input("Введите ваш логин: ")

# "глухой" цикл – получение сообщений программой
while True:
    # Получение данных
    data = sock.recv(1024)
    data = data.decode('utf-8')
    # Обработка сообщения
    if not data.startswith('online'):
        # Выводим в консоль
        print(data)
