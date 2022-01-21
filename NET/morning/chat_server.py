
import netutils
import socket
from threading import Thread

server_socket = socket.socket()
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # allow to reuse the socket if we restart the app after a crash
server_socket.bind(('0.0.0.0', 5577)) # 0.0.0.0 to listen to all interfaces (wifi, localhost, ...)
server_socket.listen()

#print(server_socket)

# this is not really a chat server, it just wait for one message from a client then waits for another client

all_clients = []

def send_to_everyone(msg, sender):
    tosend = msg+'\r\n'
    tosend = tosend.encode('utf-8')
    for sock in all_clients:
        if sock != sender:
            # should try / except/catch
            sock.sendall(tosend) # may be blocking


def handle_one_client(sock):

    def do_actually_handle_the_client():

        while True:
            l = netutils.read_line(sock) # blocking
            print("RECEIVED:", l)
            send_to_everyone('Somebody wrote said: '+l, sock)

    Thread(target=do_actually_handle_the_client).start()


while True:
    print("before accept")
    sock, addr = server_socket.accept() # blocking
    print("after accept")

    all_clients.append(sock)
    handle_one_client(sock)

print("END")
