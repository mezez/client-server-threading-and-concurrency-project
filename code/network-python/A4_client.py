import decimal
import random
import socket
import time

import netutils


def main():  # called at the end of the file
    print("Creating connection")
    s = socket.create_connection(('localhost', 9999))
    print("created", s)

    message_count = 0
    while message_count < 50:
        time.sleep(decimal.Decimal(random.randrange(1, 99)) / 100)
        send_magic_word(s)
        message_count = message_count + 1

    s.close()

    # while True:
    #     l = netutils.read_line(s)
    #     print("got reply:", l)


def send_magic_word(socket):
    # s.sendall(b'HI FROM SIMPLE CLIENT\r\n')
    socket.send(b'magic\r\n')
    print("sent magic word")


if __name__ == "__main__":
    main()
