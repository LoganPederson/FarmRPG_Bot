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


class PepperBot:
    def __init__(self):
        # initialize the WindowCapture class
        self.exitPlease = False
        self.wincap = WindowCapture()
        # initialize the Vision class
        self.nextButton = Vision('img/next_button.jpg')
        self.notYet = Vision('img/not_yet.jpg')
        self.plantSeedButton = Vision('img/plantButton.jpg')
        self.harvestableOnion = Vision('img/harvestableOnion.jpg')
        self.harvestBarGreen = Vision('img/harvestBarGreen.jpg')
        self.tooSoon = Vision('img/tooSoon.jpg')
        self.pepperReady = Vision('img/pepperReady.jpg')
        self.radishReady = Vision('img/radishReady.jpg')
        self.carrotReady = Vision('img/carrotReady.jpg')
        self.cancelButton = Vision('img/cancelButton.jpg')
        self.outOfSeeds = Vision('img/outOfSeeds.jpg')
        self.town_text = Vision('img/town_img.jpg')
        self.store_text = Vision('img/store_text.jpg')
        self.pepper_buy = Vision('img/pepper_buy.jpg')
        self.market_text = Vision('img/market_text.jpg')
        self.sell_crops_text = Vision('img/sell_crops_text.jpg')
        self.refreshWindowTimer = time()
        self.loop_time = time()
    def exitApp(self):
        # If button pressed, destroy the window
        self.exitPlease = True
        
    def main(self):
        while(self.exitPlease == False):
            # get an updated image of the game
            screenshot = self.wincap.get_screenshot()
            #show screenshot
            #cv.imshow('screenshot', screenshot)

            # display the processed image
            #points = nextButton.find(screenshot, 0.95, 'rectangles')
            plantSeed = self.plantSeedButton.find(screenshot, 0.9, 'points')
            if (plantSeed.any()):
                print(plantSeed)
                print("Detected plant seed button")
                pyautogui.click(1212, 211) # CLICK PLANT ALL
                sleep(1.3)
                pyautogui.click(963, 963) # CLICK YES
                sleep(1.3)
                print("Done planting 4x4")
                print("Rebuying seeds...")
                pyautogui.click(116, 180) # CLICK HOME
                sleep(1.3)
                screenshot = self.wincap.get_screenshot() # CLICK MARKET
                click_town = self.town_text.find(screenshot, 0.7, 'points')
                sleep(1.3)
                print('looking for town ')
                if (click_town.any()):
                    find_market_clickpoint = self.town_text.get_click_points(click_town)
                    for clickpoint in find_market_clickpoint:
                        pyautogui.click(clickpoint[0], clickpoint[1])
                        print('found clickpoint of town_text of: '+str(clickpoint[0])+ ' '+ str(clickpoint[1]))
                        break
                else:
                    print('no market found')
                    break
                sleep(1.3)
                screenshot = self.wincap.get_screenshot() # GOTO STORE
                click_store = self.store_text.find(screenshot, 0.7, 'points') 
                if (click_store.any()):
                    find_store_clickpoint = self.store_text.get_click_points(click_store)
                    for clickpoint in find_store_clickpoint:
                        pyautogui.click(clickpoint[0], clickpoint[1])
                        print('found clickpoint of store_text of: '+str(clickpoint[0])+ ' '+ str(clickpoint[1]))
                        break
                else:
                    print('no store found')
                    break
                sleep(1.3)
                screenshot = self.wincap.get_screenshot() # CLICK BUY
                buy_pepper = self.pepper_buy.find(screenshot, 0.9, 'points')
                if (buy_pepper.any()):
                    buy_pepper_clickpoints = self.pepper_buy.get_click_points(buy_pepper)
                    for clickpoint in buy_pepper_clickpoints:
                        pyautogui.click(clickpoint[0]+1100, clickpoint[1]+40)
                        print('found clickpoint of buy_pepper of: '+str(clickpoint[0])+ ' '+ str(clickpoint[1]))
                        break
                else:
                    print('no buy_pepper found')
                    break
                sleep(3)
                pyautogui.click(960, 965) # CLICK OK
                sleep(3)
                pyautogui.click(966, 564) # CLICK GO TO FARM
                # longer sleep as 1 second would catch the screen half way swapped and mis-click then rebuy in error
                sleep(3)

            #Get updated screenshot as searching for plantSeed may have taken a bit of time
            screenshot = self.wincap.get_screenshot()
            harvest = self.pepperReady.find(screenshot, 0.90, 'points') # [CARROT 0.90, RADISH x.xx]
            if (harvest.any()):
                print("harvastable found, harvesting!")
                print(harvest)
                pyautogui.click(575, 211) # CLICK HARVEST ALL
                sleep(3.3)
                print("Done harvesting 4x4, replanting...")
                pyautogui.click(1216, 209)# CLICK PLANT ALL
                sleep(1.3)
                pyautogui.click(963, 963) # CLICK YES
                sleep(3.3)
                print("Done replanting")
                #sell all the crops and rebuy more
                pyautogui.click(116, 180) # CLICK HOME
                sleep(1.5)
                print('looking for town ')
                screenshot = self.wincap.get_screenshot() # CLICK TOWN
                click_town = self.town_text.find(screenshot, 0.8, 'points')
                if (click_town.any()):
                    find_town_clickpoint = self.town_text.get_click_points(click_town)
                    for clickpoint in find_town_clickpoint:
                        pyautogui.click(clickpoint[0], clickpoint[1])
                        print('found clickpoint of town_text of: '+str(clickpoint[0])+ ' '+ str(clickpoint[1]))
                        break
                else:
                    print('no town found')
                    break
                sleep(1.3)
                print('looking for market ')
                screenshot = self.wincap.get_screenshot() # CLICK MARKET
                click_market = self.market_text.find(screenshot, 0.8, 'points')
                if (click_market.any()):
                    find_market_clickpoint = self.market_text.get_click_points(click_market)
                    for clickpoint in find_market_clickpoint:
                        pyautogui.click(clickpoint[0], clickpoint[1])
                        print('found clickpoint of market_text of: '+str(clickpoint[0])+ ' '+ str(clickpoint[1]))
                        break
                else:
                    print('no market found')
                    break
                sleep(1.3)
                screenshot = self.wincap.get_screenshot() # CLICK SELL ALL CROPS
                click_sell_all_crops = self.sell_crops_text.find(screenshot, 0.75, 'points')
                if (click_sell_all_crops.any()):
                    find_sell_clickpoint = self.sell_crops_text.get_click_points(click_sell_all_crops)
                    for clickpoint in find_sell_clickpoint:
                        pyautogui.click(clickpoint[0], clickpoint[1]+20)
                        print('found clickpoint of sell_crops_text of: '+str(clickpoint[0])+ ' '+ str(clickpoint[1]))
                        break
                else:
                    print('no sell_crops_text found')
                    break 
                sleep(1.3)
                pyautogui.click(960, 960) # CLICK YES
                sleep(3.5)
                pyautogui.click(958, 607) # CLICK OK
                sleep(3.5)
                pyautogui.click(116, 180) # CLICK HOME
                sleep(3)
                print('looking for town ') # CLICK TOWN
                screenshot = self.wincap.get_screenshot()
                click_town = self.town_text.find(screenshot, 0.8, 'points')
                if (click_town.any()):
                    find_town_clickpoint = self.town_text.get_click_points(click_town)
                    for clickpoint in find_town_clickpoint:
                        pyautogui.click(clickpoint[0], clickpoint[1])
                        print('found clickpoint of town_text of: '+str(clickpoint[0])+ ' '+ str(clickpoint[1]))
                        break
                else:
                    print('no town found')
                    break
                sleep(2)
                screenshot = self.wincap.get_screenshot()
                click_store = self.store_text.find(screenshot, 0.8, 'points') 
                if (click_store.any()):
                    find_store_clickpoint = self.store_text.get_click_points(click_store)
                    for clickpoint in find_store_clickpoint:
                        pyautogui.click(clickpoint[0], clickpoint[1])
                        print('found clickpoint of store_text of: '+str(clickpoint[0])+ ' '+ str(clickpoint[1]))
                        break
                else:
                    print('no store found')
                    break
                sleep(1.3)
                screenshot = self.wincap.get_screenshot() # CLICK BUY
                buy_pepper = self.pepper_buy.find(screenshot, 0.9, 'points')
                if (buy_pepper.any()):
                    buy_pepper_clickpoints = self.pepper_buy.get_click_points(buy_pepper)
                    for clickpoint in buy_pepper_clickpoints:
                        pyautogui.click(clickpoint[0]+1100, clickpoint[1]+40)
                        print('found clickpoint of buy_pepper of: '+str(clickpoint[0])+ ' '+ str(clickpoint[1]))
                        break
                else:
                    print('no buy_pepper found')
                    break
                sleep(2.5)
                pyautogui.click(960, 960) # CLICK YES
                sleep(2.5)
                pyautogui.click(960, 560) # CLICK GO TO FARM [FROM COUNTRY STORE MENU]
                # longer sleep as 1 second would catch the screen half way swapped and mis-click then rebuy in error
                sleep(2.5)
                
            #Click to remove popup window that may appear
            clickPopup = self.tooSoon.find(screenshot, 0.9, 'points')
            if(clickPopup.any()):
                pyautogui.click(966, 596)
                print("Clicked at 966, 596 to remove popup window if present")
            #Click to remove cancel window that may appear and cause a loop
            clickCancel = self.cancelButton.find(screenshot, 0.8, 'points')
            if(clickCancel.any()):
                pyautogui.click(960, 1009)
                print("Clicked at 960, 1009 to remove cancel window")
            #check to see if out of seeds, rebuy if so
            if(self.outOfSeeds.find(screenshot, 0.9, 'points').any()):
                pyautogui.click(116, 180) # CLICK HOME
                sleep(2)
                pyautogui.click(289, 524) # CLICK GO TO TOWN [NORMAL 535,430] [BANNER 289, 524]
                sleep(2)
                pyautogui.click(508, 318) # CLICK MARKET 
                sleep(3)
                pyautogui.click(1478, 382) # CLICK BUY -> CARROT SET [PEPPER: 1478, 382] [CARROT: 1478, 498]
                sleep(3)
                pyautogui.click(960, 965) # CLICK YES
                sleep(3)
                pyautogui.click(960, 560) # CLICK GO TO FARM [FROM COUNTRY STORE MENU]
                # longer sleep as 1 second would catch the screen half way swapped and mis-click then rebuy in error
                sleep(2.5)
                

            #refreshWindowTimer 
            # if (time() - self.refreshWindowTimer > 240):
            #     sleep(3.5)
            #     pyautogui.click(1010, 80)
            #     print("Clicked at 1010, 80 on bookmark button")
            #     sleep(3.5)
            #     self.refreshWindowTimer = time()
            #     pyautogui.click(116, 185) # CLICK HOME
            #     print("Clicked at 116, 185 on home button to refresh")
            #     sleep(3.5)
            #     pyautogui.click(490, 330) # CLICK GO TO FARM [NORMAL 465,253] [BANNER 490,330]
            #     print("Clicked at 465, 253 to return to farm")
            #     sleep(3.5)


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
