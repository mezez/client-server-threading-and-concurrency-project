import queue
from threading import Thread
import socket
import time
import display
from netutils import read_line
import random

# magic word
magic_word = "magic"


def main():  # called at the end of the file
    d = display.Display()

    q = queue.Queue()
    c = consumer(d, q)

    c.daemon = True  # the program terminates when all non daemon threads are done
    c.start()

    time.sleep(1)
    n = 10
    for i in range(n):
        time.sleep(random.uniform(0, 0.001))
        #producer(q).start()

    time.sleep(5)  # do not finish right away (so we can see if the consumer prints)


    # start a new thread to accept new connections
    handle_acceptall(d, q).start()


def handle_acceptall(display, my_queue):
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
            handle_client(s, display, my_queue).start()

    t = Thread(target=handle)
    return t


# handle_client returns a Thread that can be started, i.e., use: handle_client(.......).start()
# producer
def handle_client(socket, display, my_queue):
    def handle(): #add elements to queue
        # initialise a random integer position, e.g. between 0 and 100
        i = random.randint(1, 10)

        # initialize a random direction (for later)
        by = random.choice([-1, 1])

        # add 1 to the display, at index i (and render it)
        #display.add_value(i, 1)
        #display.render()

        my_queue.put((i, 1, None))
        my_queue.put("RENDER")

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
                    #display.move_value_right(i, direction, 1)
                    #display.render()

                    my_queue.put((i, direction, 1))
                    my_queue.put("RENDER")

                    i += direction

        # Later, we will use move_value_right(i, by) and increase the i variable by
        # ???

        # when the connection is closed, subtract at index (and rerender)
        #display.add_value(i, -1)
        #display.render()

        my_queue.put((i, -1, None))
        my_queue.put("RENDER")

    t = Thread(target=handle)
    return t

# def producer(q):
#     def add_elements():
#         for iteration in range(100):
#             i = random.randrange(20)
#             q.put((i, 1))
#             time.sleep(random.uniform(0, 0.002))
#             q.put((i, -1))
#         q.put("RENDER")
#
#     t = Thread(target=add_elements)
#     return t


def consumer(d, q):
    def consume():
        while True:
            e = q.get()
            if e == "RENDER":
                d.render()
            else:
                i, v, direction = e
                if direction is None:
                    d.add_value(i, v)
                else:
                    d.move_value_right(i, direction, v)

    t = Thread(target=consume)
    return t


def is_magic_word(word):
    if word == magic_word:
        return True
    return False


if __name__ == "__main__":
    main()
