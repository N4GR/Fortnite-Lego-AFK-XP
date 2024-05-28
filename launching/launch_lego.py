import pyautogui
import time
from random import randint

from screeninfo import get_monitors

import json

import keyboard
import os

import cv2
import easyocr

for m in get_monitors():
    if m.is_primary is True:
        monitor = m

with open(f"launching/launch_pos/{monitor.height}.json") as f:
    positions = json.load(f)

with open(f"launching/launch_pos/{monitor.height}conf.json") as f:
    crop_coords = json.load(f)

def checks():
    print("Welcome to the Lego Fortnite launching section, we need to check a few things; 0 for no, 1 for yes.")
    while True:
        free_world = input("\n Do you have a free slave slot for creating a world? ")
        if free_world == "0":
            print("This script won't work without one, make a free slot available.\n")
        elif free_world == "1":
            break
        else:
            print("Please input either a 1 or a 0. 1 for yes, 0 for no.")
    
    while True:
        selection = input("\n Do you have Lego Fortnite currently selected? ")
        if selection == "1":
            print("\n For the script to work, you need to not have lego fortnite currently selected; enter into a different mode before begining.")
        elif selection == "0":
            break
        else:
            print("Please input either a 1 or a 0. 1 for yes, 0 for no.")
    
    print("\nTo exit the script, hold down q for 10 seconds until it stops.")

    for x in range(5):
        print(f"Beginning in {5 - x} seconds.")
        if keyboard.is_pressed("q"):
            print("Quitting program...")
            os._exit(0)

        time.sleep(1)
    
    print("\n\n")

def wait():
    time.sleep(1)

def check_complete():
    img1 = pyautogui.screenshot(region=(crop_coords["quest"][0], crop_coords["quest"][1], crop_coords["quest"][2], crop_coords["quest"][3]))
    img1.save("dump/screenshot.png")
    img = cv2.imread("dump/screenshot.png")

    # Text detect instance
    reader = easyocr.Reader(["en"], gpu = False, verbose = False)

    # Detect text
    detect = reader.readtext(img)

    if not detect:
        return False
    else:
        for t in detect:
            bbox, text, score = t

            if text == "Quest":
                return True

def main():
    checks()

    for position in positions:
        if keyboard.is_pressed("q"):
            print("Quitting program...")
            os._exit(0)
            
        x = randint(positions[position][0], positions[position][0] + 5)
        y = randint(positions[position][1], positions[position][1] + 5)

        print(f"Dragging to x: {x}, y: {y} from dict = {position}...")
        pyautogui.dragTo(x, y)
        wait()
        wait()
        print(f"clicking x: {x}, y: {y}...")
        pyautogui.click()
        wait()

        if positions[position] == positions["search_box"]:
            print("Pressing ctrl + a...")
            pyautogui.hotkey("ctrl", "a")
            wait()
            print("Typing Lego Fortnite...")
            pyautogui.typewrite("Lego Fortnite", interval = 0.1)
            wait()
            print("Pressing Enter...")
            pyautogui.press("enter")
            wait()
    

    times_tries = 0
    while True:
        times_tries =+ 1
        print(f"Checking if in game, tried {times_tries} time/s.")
        if check_complete() is True:
            break
        time.sleep(5)