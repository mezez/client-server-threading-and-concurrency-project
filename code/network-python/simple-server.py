import socket

server_socket = socket.socket()
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #allow reuse of address if server is restarted
server_socket.bind(('0.0.0.0', 5577)) #0.0.0.0 to listen to all interfaces (wifi, localhost)
server_socket.listen()
print(server_socket)

while True:
    print("waiting for connection")
    s, addr = server_socket.accept() #blockiig
    print("received connection", s)