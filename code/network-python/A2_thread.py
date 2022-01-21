
from threading import Thread
import time
import random
import display

def main():
    d = display.Display()

    time.sleep(0.5)
    n = 20
    for i in range(n):
        # start a producer every 300ms
        time.sleep(0.3)
        producer(d, i).run()
        producer(d, i).run()
        # replace "start" by "run" above to not start a thread (and thus test as if you were not using threads...)


def producer(d, ind):
    def add_elements():
        for iteration in range(9):
            d.add_value(ind, 1)
            time.sleep(random.uniform(0, .5)) # wait randomly, up to 500ms
            d.render_clean()

    t = Thread(target=add_elements)
    return t


if __name__== "__main__":
  main()
