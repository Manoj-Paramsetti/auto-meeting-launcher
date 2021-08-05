import os
import sys
import pyautogui
import webbrowser

files = os.listdir()


def open_zoom():
    f = open("zoom.txt", "r")
    webbrowser.open(f.readline())
    launch_zoom()


def launch_zoom():
    try:
        x, y = pyautogui.locateCenterOnScreen(
            "Zoom-Launch-Meeting-Button.png", confidence=0.8
        )
        pyautogui.click(x, y)

    except TypeError:
        print("Waiting for browser to open")
        launch_zoom()


if "zoom.txt" not in files:
    print("Paste your zoom invite link")
    link = input()
    f = open("zoom.txt", "w")
    f.write(link)

open_zoom()
