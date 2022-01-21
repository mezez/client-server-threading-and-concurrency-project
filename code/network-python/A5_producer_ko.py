
from threading import Thread
import time
import random
import display

def main(): # called at the end of the file
    d = display.Display()

    time.sleep(0.5)
    n = 10
    for i in range(n):
        time.sleep(random.uniform(0, 0.001))
        producer(d).start()

def producer(d):
    def add_elements():
        for iteration in range(100):
            i = random.randrange(20)
            d.add_value(i, 1)
            time.sleep(random.uniform(0, 0.002))
            d.add_value(i, -1)
        d.render_clean()

    t = Thread(target=add_elements)
    return t

if __name__== "__main__":
  main()
