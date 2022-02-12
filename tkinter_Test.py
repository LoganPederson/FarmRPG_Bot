from tkinter import *
import mainV2
import logCommands
from fishingAuto import FishingBot
from pepperBot import PepperBot
from mainV2 import exitPlease
import threading
from time import *
import cv2 as cv
import pyautogui
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

def buildAppleTrees():
    print('building apple trees')
    buildingAmount = 150
    i = 0
    while i < buildingAmount:
        pyautogui.click(444,476) # CLICK PLANT APPLE
        sleep(.3)
        pyautogui.click(961,959) # CLICK YES
        sleep(.3)
        pyautogui.click(964,614) # CLICK OK
        sleep(.3)
        i += 1
        print("done with apple tree %d" % i)


root = Tk()
# create geometry
root.title("FarmRPG_Bot")
root.geometry("500x100+1400+900")
# Make the window stay above all other windows
root.attributes('-topmost',True)
# Creating a Label Widget
myLabel1 = Label(root, text="Farm Peppers")
myLabel2 = Button(root, command=runPepperBot_Background, text="Click Me!")
myLabel3 = Button(root, command=stopRunningPepperBot, text="Exit")
myLabel4 = Label(root, text="Start Fishing!")
myLabel5 = Button(root, command=runFishingBot_background, text="Click Me!")
myLabel6 = Button(root, command=stopFishingBot, text="Exit!")
myLabel7 = Label(root, text="Build Apple Trees")
myLabel8 = Button(root, command=buildAppleTrees, text="Build!")
# Grid Positions:
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=0, column=1)
myLabel3.grid(row=0, column=2)
myLabel4.grid(row=1, column=0)
myLabel5.grid(row=1, column=1)
myLabel6.grid(row=1, column=2)
myLabel7.grid(row=2, column=0)
myLabel8.grid(row=2, column=1)

root.mainloop()
