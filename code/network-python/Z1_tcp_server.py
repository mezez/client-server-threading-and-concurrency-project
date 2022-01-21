import socket
import netutils

server_socket = socket.socket()
server_socket.bind(('0.0.0.0', 9999)) # 0.0.0.0 to listen to all interfaces (wifi, localhost, ...)
server_socket.listen()
print(server_socket)

# process clients one by one (not in parallel)
while True:
    print("Waiting for connection")
    client_socket, addr = server_socket.accept()
    print("Received connection", client_socket)
    # read two lines then ignore anything from this client...
    l = netutils.read_line(client_socket)
    print("RECEIVED FIRST:", l)
    l = netutils.read_line(client_socket)
    print("RECEIVED SECOND:", l)
    # ... ignore the rest
