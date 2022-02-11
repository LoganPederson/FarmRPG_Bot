import cv2 as cv
import numpy as np
import os
import pyautogui
from time import time 
from time import sleep 
from windowcapture import WindowCapture
from vision import Vision
import pyautogui
from tkinter import *
import sys
import msvcrt

class FishingBot:
    
    def __init__(self):

        self.exitPlease = False
        # initialize the WindowCapture class
        self.wincap = WindowCapture()
        # initialize the Vision class
        self.outOfSeeds = Vision('outOfSeeds.jpg')
        self.refreshWindowTimer = time()
        self.loop_time = time()


    def exitApp(self):
        # If button pressed, destroy the window
        self.exitPlease = True
        
    def main(self):  

        while(self.exitPlease == False):
            # get an updated image of the game
            self.screenshot = self.wincap.get_screenshot()


            # show screenshot
            #cv.imshow('screenshot', screenshot)

            # display the processed image
        

            #refreshWindowTimer 
            if (time() - self.refreshWindowTimer > 240):
                sleep(3.5)
                pyautogui.click(1010, 80)
                print("Clicked at 1010, 80 on bookmark button")
                sleep(3.5)
                self.refreshWindowTimer = time()
                pyautogui.click(116, 185)
                print("Clicked at 116, 185 on home button to refresh")
                sleep(3.5)
                pyautogui.click(465, 253)
                print("Clicked at 465, 253 to return to farm")
                sleep(3.5)


            # debug the loop rate
            print('FPS {}'.format(1 / (time() - self.loop_time)))
            self.loop_time = time()

            # press 'q' with the output window focused to exit.
            # waits 1 ms every loop to process key presses
            if cv.waitKey(1) == ord('q'):
                cv.destroyAllWindows()
                break
            if self.exitPlease == True:
                cv.destroyAllWindows()
                break

        print('Done.')
