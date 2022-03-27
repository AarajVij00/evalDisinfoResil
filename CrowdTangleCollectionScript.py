### Tom Plant and Aaraj Vij
### 03/25/2022
### This script downloads CrowdTangle
### data on specified URLs

import pyautogui #For controlling mouse and key strokes
import pandas as pd #For reading in .csv file
import time #For delays in mouse clicks

## Retrieve list of URLs to collect data from
urlsDF = pd.read_csv("FILE PATH HERE") # Replace with file to read of URLs to read in
urlList = urlsDF['URL'].tolist()

## Open Chrome on computer
## Configured for HP Spectre, 15" computer
pyautogui.moveTo(1000, 2200)
pyautogui.click()

## Download CrowdTangle data from each URL
for i in range(len(urlList)):
        pyautogui.moveTo(500, 110) # Navigate to URL bar
        pyautogui.click()

        pyautogui.keyDown("ctrl") # Delete current URL
        pyautogui.press("a")
        pyautogui.keyUp("ctrl")
        pyautogui.press("backspace")

        pyautogui.write(urlList[i]) # Navigate to next URL
        pyautogui.press('return')
        time.sleep(4)

        pyautogui.moveTo(3500, 110) # Click on CrowdTangle extension
        time.sleep(5)
        pyautogui.click()
        pyautogui.moveTo(3400, 310) # Download data from CrowdTangle extension
        time.sleep(4)
        pyautogui.click()
        time.sleep(3)