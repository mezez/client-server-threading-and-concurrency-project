
import socket
import netutils
from threading import Thread

server_socket = socket.socket()
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # allow to reuse the socket if we restart the app after a crash
server_socket.bind(('0.0.0.0', 5577)) # 0.0.0.0 to listen to all interfaces (wifi, localhost, ...)
server_socket.listen()
#print(server_socket)

def handle_client(s):

    def actually_do_handle_client():
        while True:
            l = netutils.read_line(s) # blocking
            print("RECEIVED:", l)
            tosend = 'You said: '+l+'\r\n'
            tosend = tosend.encode('utf-8')
            s.sendall(tosend) # may be blocking

    t = Thread(target=actually_do_handle_client)
    t.start()
    
while True:
    print("Waiting for connection")
    s, addr = server_socket.accept() # blocking
    print("Received connection")

    handle_client(s)
