import time
import threading

from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode, Key
#from tkinter import *


TOGGLE_KEY = Key.f6

#root = Tk()


#myLabel = Label(root, text="Hello World!")


#myLabel.pack()


#root.mainloop()



##### breaks stuff :cry:




clicking = False
mouse = Controller()


def clicker():
    while True:
        if clicking:
            mouse.click(Button.left, 1)
        time.sleep(0.001)


def toggle_event(key):
    if key == TOGGLE_KEY:
        global clicking
        clicking = not clicking
        if clicking:
            print("Clicking")
        else:
            print("Not Clicking")


click_thread = threading.Thread(target=clicker)
click_thread.start()

with Listener(on_press=toggle_event) as listener:
    listener.join()
