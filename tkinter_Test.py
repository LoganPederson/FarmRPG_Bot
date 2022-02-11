from tkinter import *
import mainV2
from fishingAuto import FishingBot
from pepperBot import PepperBot
from mainV2 import exitPlease
import threading
import time
import cv2 as cv

# Create a window
fishingBot = FishingBot()
pepperBot = PepperBot()



def runFishingBot():
    fishingBot.exitPlease = False
    fishingBot.main()

    # run exitApp from mainV2 file

def runFishingBot_background():
    f = threading.Thread(target=runFishingBot)
    f.start()
    

def runPepperBot():
    pepperBot.exitPlease = False
    pepperBot.main()

def runPepperBot_Background():
    p = threading.Thread(target=runPepperBot)
    p.start()

def stopRunningPepperBot():
    pepperBot.exitApp()
    print('exiting pepper bot')
    
def stopFishingBot():
    fishingBot.exitApp()
    print('exiting fishing bot')



root = Tk()
# create geometry
root.title("FarmRPG_Bot")
root.geometry("500x100+1400+900")
# Creating a Label Widget
myLabel1 = Label(root, text="Run Main")
myLabel2 = Button(root, command=runPepperBot_Background, text="Click Me!")
myLabel3 = Button(root, command=stopRunningPepperBot, text="Exit")
myLabel4 = Label(root, text="Start Fishing!")
myLabel5 = Button(root, command=runFishingBot_background, text="Click Me!")
myLabel6 = Button(root, command=stopFishingBot, text="Exit!")
# Grid Positions:
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=0, column=1)
myLabel3.grid(row=0, column=2)
myLabel4.grid(row=1, column=0)
myLabel5.grid(row=1, column=1)
myLabel6.grid(row=1, column=2)
root.mainloop()
