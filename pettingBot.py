import cv2 as cv
import numpy as np
import os
import pyautogui
from time import time 
from time import sleep
from time import ctime 
from windowcapture import WindowCapture
from vision import Vision
import pyautogui
from tkinter import *
import sys
import msvcrt




class PettingBot:  

    def __init__(self):
        self.exitPlease = False
        self.wincap = WindowCapture()
        self.chicken = Vision('chicken.jpg')
    def logClickOnChicken(self):
        f = open("log.txt", "a+")
        t=time()
        currentTime = ctime(t)
        f.write("\n" + "%s Clicking on chicken"%currentTime)
        f.close()

    def exitApp(self):
        print('exiting app')
        sys.exit()

    def petChicken(self):
        while(self.exitPlease == False):
            screenshot = self.wincap.get_screenshot()
            chicken = self.chicken.find(screenshot, 0.9, 'points')
            if chicken.any:
                findChickenClickpoint = self.chicken.get_click_points(chicken)
                sleep(.2)
                for clickpoint in findChickenClickpoint:
                    pyautogui.click(clickpoint[0], clickpoint[1])
                    self.logClickOnChicken()
                    sleep(1)
                    pyautogui.click(410, 510) # PET CHICEKN
                    sleep(1)
                    pyautogui.click(960, 610) # CLICK OK
                    sleep(1)
    def buyChickens(self, amount):
        i = 0
        while i < amount:
            print('buying chickens')
            pyautogui.click(675, 345) # CLICK BUY CHICKENS
            sleep(1)
            pyautogui.click(965, 965) # CLICK YES
            sleep(1)
            pyautogui.click(960, 610) # CLICK OK
            sleep(1)
            print("just purchased chicken %d"%chicken)
            i += 1
        