
import socket
import queue
import time

class Display:
    def __init__(self, N=30):
        self.values = [0 for i in range(N)]

    def add_value(self, i, v=1):
        nv = self.values[i%len(self.values)] + v
        time.sleep(.001) # simulate a computation that takes some time (to illustrate thing about threads later)
        self.values[i%len(self.values)] = nv

    def move_value_right(self, i, by=1, v=1):
        self.add_value(i, -v)
        self.add_value(i+by, v)

    def render(self):
        print("".join(['%2d'%(v,) for v in self.values]), "->", sum(self.values))

    def render_clean(self):
        print("".join(["  " if v==0 else " ." if v==1 else ("   "+str(v))[-2:] for v in self.values]), "->", sum(self.values))
