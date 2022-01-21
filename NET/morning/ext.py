import netutils

def external_process_client(sock):
    while True:
        l = netutils.read_line(sock) # blocking
        print("RECEIVED:", l)

        tosend = 'You wrote: '+l+'\r\n'
        tosend = tosend.encode('utf-8')
        sock.sendall(tosend) # may be blocking
        #sock.close()
