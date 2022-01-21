from threading import Thread
import socket
import display
from netutils import read_line
import random

# magic word
magic_word = "magic"


def main():  # called at the end of the file
    d = display.Display()
    # start a new thread to accept new connections
    handle_acceptall(d).start()


def handle_acceptall(display):
    def handle():
        # create a socket that listens (on a port of your choice)
        server_socket = socket.socket()
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind(('0.0.0.0', 9999))
        server_socket.listen()
        print(server_socket)
        print('waiting for connection')

        # accept new clients connections,
        while True:
            s, addr = server_socket.accept()  # blocking
            print('received connection', s)

            # and start a handle_client thread every time
            handle_client(s, display).start()

    t = Thread(target=handle)
    return t


# handle_client returns a Thread that can be started, i.e., use: handle_client(.......).start()
def handle_client(socket, display):
    def handle():
        # initialise a random integer position, e.g. between 0 and 100
        i = random.randint(1, 10)

        # initialize a random direction (for later)
        by = random.choice([-1, 1])

        # add 1 to the display, at index i (and render it)
        display.add_value(i, 1)
        display.render()

        # loop over the received data, ignoring (or just printing) this data for now (e.g., use netutils to read lines)
        # be sure to end the loop when the connection is closed (readLine returns None or throws an exception)
        while True:
            line = read_line(socket)
            if line is None:
                break
            else:
                print("received", line)
                if is_magic_word(line):
                    direction = random.choice([-1, 1])
                    display.move_value_right(i, direction, 1)
                    display.render()
                    i += direction

        # Later, we will use move_value_right(i, by) and increase the i variable by
        # ???

        # when the connection is closed, subtract at index (and rerender)
        display.add_value(i, -1)
        display.render()

    t = Thread(target=handle)
    return t


def is_magic_word(word):
    if word == magic_word:
        return True
    return False


if __name__ == "__main__":
    main()
