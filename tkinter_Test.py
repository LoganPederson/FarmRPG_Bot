from tkinter import *
import mainV2
import logCommands
from fishingAuto import FishingBot
from pepperBot import PepperBot
from pettingBot import PettingBot
from peaBot import PeaBot
from exploringBot import ExploreBot
from mainV2 import exitPlease
import threading
from time import *
import cv2 as cv
import pyautogui
# Create a window
fishingBot = FishingBot()
pepperBot = PepperBot()
pettingBot = PettingBot()
peaBot = PeaBot()
exploreBot = ExploreBot()


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

def runPeaBot():
    peaBot.exitPlease = False
    peaBot.main()

def runPeaBot_Background():
    p = threading.Thread(target=runPeaBot)
    p.start()

def runExploreBot():
    exploreBot.exitPlease = False
    exploreBot.main()

def runExploreBot_Background():
    p = threading.Thread(target=runExploreBot)
    p.start()


def stopRunningPepperBot():
    pepperBot.exitApp()
    print('exiting pepper bot')
    
def stopFishingBot():
    fishingBot.exitApp()
    print('exiting fishing bot')

def stopRunningPeaBot():
    peaBot.exitApp()
    print('exiting pea bot')

def stopRunningExploreBot():
    exploreBot.exitApp()
    print('exiting explore bot')    

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

def runPettingChickens():
    pettingBot.petChicken()

def buyingChickens(amount):
    pettingBot.buyChickens(amount)

root = Tk()
# create geometry
root.title("FarmRPG_Bot")
root.geometry("500x1500+1400+850")
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
myLabel9 = Label(root, text="Pet Chickens")
myLabel10 = Button(root, command=runPettingChickens, text="Pet!")
myLabel11 = Label(root, text="Farm Peas")
myLabel12 = Button(root, command=runPeaBot_Background, text="Click Me!")
myLabel13 = Button(root, command=stopRunningPeaBot, text="Exit")
myLabel14 = Label(root, text="Explore!")
myLabel15 = Button(root, command=runExploreBot_Background, text="Click Me!")
myLabel16 = Button(root, command=stopRunningExploreBot, text="Exit")
# myLabel11 = Entry(root, text="Enter Amount of Chickens to Buy")
# amountOfChickens = myLabel11.get()
# intAmount = int(amountOfChickens)
# myLabel12 = Button(root, text="Buy Chickens!", command=buyingChickens(intAmount))


# Grid Positions:
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=0, column=1)
myLabel3.grid(row=0, column=2)
myLabel4.grid(row=1, column=0)
myLabel5.grid(row=1, column=1)
myLabel6.grid(row=1, column=2)
myLabel7.grid(row=2, column=0)
myLabel8.grid(row=2, column=1)
myLabel9.grid(row=3, column=0)
myLabel10.grid(row=3, column=1)
myLabel11.grid(row=4, column=0)
myLabel12.grid(row=4, column=1)
myLabel13.grid(row=4, column=2)
myLabel14.grid(row=5, column=0)
myLabel15.grid(row=5, column=1)
myLabel16.grid(row=5, column=2)
# myLabel11.grid(row=3, column=2)
# myLabel12.grid(row=3, column=3)

root.mainloop()
