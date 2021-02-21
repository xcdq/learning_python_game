import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
x = input('x: ')
y = input('y: ')
data = str(x)+','+str(y)
s.sendto(data.encode('utf-8'), ('127.0.0.1', 8888))
data2, addr = s.recvfrom(1024)
print('recv: ', data2.decode('utf-8'))
s.close()
