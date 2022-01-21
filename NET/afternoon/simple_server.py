
import socket
import netutils

server_socket = socket.socket()
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # allow to reuse the socket if we restart the app after a crash
server_socket.bind(('0.0.0.0', 5577)) # 0.0.0.0 to listen to all interfaces (wifi, localhost, ...)
server_socket.listen()
#print(server_socket)

while True:
    print("Waiting for connection")
    s, addr = server_socket.accept() # blocking
    print("Received connection")


    l = netutils.read_line(s) # blocking
    print("RECEIVED:", l)
    tosend = 'You said: '+l+'\r\n'
    tosend = tosend.encode('utf-8')
    s.sendall(tosend) # may be blocking

    # force close the connection so that we can process another client...
    s.close()
