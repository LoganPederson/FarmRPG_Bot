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
# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub

# root = Tk()
# # create a window
# root.title("Garden Simulator")
# root.geometry("500x500")

# # create a label widget
# myLabel1 = Label(root, text="Click to Exit")
# myLabel2 = Button(root, text="!", command=exitApp)
# # Grid Positions:
# myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=0, column=1)
# root.mainloop()


class ExploreBot:
    def __init__(self):
        # initialize the WindowCapture class
        self.exitPlease = False
        self.wincap = WindowCapture()
        # initialize the Vision class
        self.cancelButton = Vision('img/cancelButton.jpg')
        self.drinkOrangeJuice = Vision('img/drinkOrangeJuice.jpg')
        self.canePoleRidge = Vision('img/canePoleRidge.jpg')
        self.exploreTheArea = Vision('img/exploreTheArea.jpg')
        self.drinkOneCoords = (960,780)
        self.refreshWindowTimer = time()
        self.drinkOrangeJuiceTimer = time()
        self.loop_time = time()
    def exitApp(self):
        # If button pressed, destroy the window
        self.exitPlease = True
        
    def main(self):
        while(self.exitPlease == False):
            # get an updated image of the game
            screenshot = self.wincap.get_screenshot()


            pyautogui.click(896,326) # CLICK TO EXPLORE
            sleep(.1) # PAUSE BEFORE CLICKING AGAIN


            drinkOrangeJuice = self.drinkOrangeJuice.find(screenshot, 0.96, 'rectangles')            
            if(drinkOrangeJuice.any()):
                print("Found OrangeJuice")
                if(time() - self.drinkOrangeJuiceTimer > 75):
                    clickPoints = self.drinkOrangeJuice.get_click_points(drinkOrangeJuice)
                    for clickPoint in clickPoints:
                        pyautogui.click(clickPoint[0], clickPoint[1]+30) # CLICK TO DRINK ORANGE JUICE, ADD 30 to Y TO CLICK PROPER SPOT
                        sleep(2)
                        pyautogui.click(self.drinkOneCoords)
                        self.drinkOrangeJuiceTimer = time()
                        sleep(2)
            #refreshWindowTimer 
            if (time() - self.refreshWindowTimer > 660):
                sleep(3.5)
                pyautogui.click(1010, 80) # CLICK BOOKMARK BUTTON
                print("Clicked at 1010, 80 on bookmark button")
                sleep(3.5)
                self.refreshWindowTimer = time()
                pyautogui.click(116, 185) # CLICK HOME
                print("Clicked at 116, 185 on home button to refresh")
                sleep(3.5)
                exploreTheArea = self.exploreTheArea.find(screenshot, 0.95, 'rectangles')
                if(exploreTheArea.any()):
                    clickPoints = self.exploreTheArea.get_click_points(exploreTheArea)
                    sleep(3)
                    for clickPoint in clickPoints:
                        pyautogui.click(clickPoint[0], clickPoint[1]) # IF EXPLORE THE AREA IS FOUND, CLICK IT
                        sleep(3)
                    canePoleRidge = self.canePoleRidge.find(screenshot, 0.95, 'rectangles')
                    if(canePoleRidge.any()):
                        clickPoints = self.canePoleRidge.get_click_points(canePoleRidge)
                        for clickPoint in clickPoints:
                            pyautogui.click(clickPoint[0], clickPoint[1]) # IF CANE POLE RIDGE IS FOUND, CLICK IT
                            sleep(3)
                        print("Done Refreshing exploringBot")
                        
                    


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
