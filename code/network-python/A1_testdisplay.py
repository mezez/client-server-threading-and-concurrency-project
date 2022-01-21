
import time
import display

def main(): # called at the end of the file
    d = display.Display()

    d.add_value(10, 2)
    d.render()

    time.sleep(2)

    i = 6
    d.add_value(i, 4)
    d.render()

    time.sleep(1)

    for iteration in range(1, 100):
        d.move_value_right(i, 1, 4)
        i += 1
        d.render()
        time.sleep(0.010)

    print()
    d.add_value(5, 1)
    d.render_clean()
    d.render()
    d.render_clean()
    d.render()



if __name__== "__main__":
  main()
