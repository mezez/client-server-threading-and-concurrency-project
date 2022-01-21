
import socket

s = socket.create_connection(('localhost', 9999))
print(s)

s.sendall(b'HELLO\r\n')

s.sendall(b'HO HO HO\r\n')

s.sendall(b'whatev\r\n')
