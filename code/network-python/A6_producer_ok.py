
from threading import Thread
import time
import random
import display
import queue


def main(): # called at the end of the file
    d = display.Display()

    q = queue.Queue()

    c = consumer(d, q)
    c.daemon = True # NB: the program terminates when all non-daemon thread are done
    c.start()

    time.sleep(1)
    n = 10
    for i in range(n):
        time.sleep(random.uniform(0, 0.001))
        producer(q).start()

    time.sleep(5) # do not finish right away (so we can see if the consumer prints)

def producer(q):
    def add_elements():
        for iteration in range(100):
            i = random.randrange(20)
            q.put((i, 1))
            time.sleep(random.uniform(0, 0.002))
            q.put((i, -1))
        q.put("RENDER")

    t = Thread(target=add_elements)
    return t


def consumer(d, q):
    def consume():
        while True:
            e = q.get()
            if e == "RENDER":
                d.render_clean()
            else:
                i, v = e
                d.add_value(i, v)

    t = Thread(target=consume)
    return t


if __name__== "__main__":
  main()
