from tkinter import *
import mainV2
from mainV2 import exitPlease
import threading
import time
import cv2 as cv

# Create a window


def runMain():
    # run the main function from mainV2.py
    mainV2.main()
    # run exitApp from mainV2 file

def runMain_background():
    t = threading.Thread(target=runMain)
    t.start()

def stopRunningMain():
    # set the variable exitPlease = True
    




root = Tk()
# Creating a Label Widget
myLabel1 = Label(root, text="Run Main")
myLabel2 = Button(root, command=runMain_background, text="Click Me!")
myLabel3 = Button(root, command=stopRunningMain, text="Exit")

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=0, column=1)
myLabel3.grid(row=0, column=2)

root.mainloop()
