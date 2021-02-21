# import socket
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(('www.dangdang.com', 80))
# s.send(b'GET / HTTP/1.1\r\nHost: www.dangdang.com\r\nConnection: close\r\n\r\n')

# buff = []
# while True:
#     d = s.recv(1024)
#     if d:
#         buff.append(d)
#     else:
#         break
# data = b''.join(buff)
# s.close()
# header, html = data.split(b'\r\n\r\n', 1)
# print(header.decode('utf-8'))
# with open('html/dang.html', 'wb') as f:
#     f.write(html)


import socket
import threading
import time


def tcplink(sock, addr):
    print('from %s:%s start' % addr)
    sock.send(b'welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('hello,%s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('from %s:%s close' % addr)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 8888))
s.listen()
while True:
    sock, addr = s.accept()
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
