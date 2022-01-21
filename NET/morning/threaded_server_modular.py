
import netutils
import socket
from threading import Thread

server_socket = socket.socket()
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # allow to reuse the socket if we restart the app after a crash
server_socket.bind(('0.0.0.0', 5577)) # 0.0.0.0 to listen to all interfaces (wifi, localhost, ...)
server_socket.listen()

#print(server_socket)

# this is not really a chat server, it just wait for one message from a client then waits for another client

from ext import external_process_client


while True:
    print("before accept")
    sock, addr = server_socket.accept() # blocking
    print("after accept")

    #square = lambda a: a**2

    Thread(target=lambda: external_process_client(sock)).start()

print("END")
