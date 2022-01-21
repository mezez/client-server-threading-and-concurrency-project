
import netutils
import socket


server_socket = socket.socket()
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # allow to reuse the socket if we restart the app after a crash
server_socket.bind(('0.0.0.0', 5577)) # 0.0.0.0 to listen to all interfaces (wifi, localhost, ...)
server_socket.listen()

#print(server_socket)

# this is not really a chat server, it just wait for one message from a client then waits for another client

while True:
    print("before accept")
    sock, addr = server_socket.accept() # blocking
    print("after accept")

    l = netutils.read_line(sock) # blocking
    print("RECEIVED:", l)

    tosend = 'You wrote: '+l+'\r\n'
    tosend = tosend.encode('utf-8')
    sock.sendall(tosend) # may be blocking
    sock.close()

print("END")
