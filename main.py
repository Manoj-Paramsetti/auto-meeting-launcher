import os
import re
import sys
import webbrowser

import yaml
import pyautogui
import tkinter

meetings = {"meetings": []}


def open_zoom_link(link):
    webbrowser.open(link)
    f.close()
    print(" Waiting for browser to open", end="")
    launch_zoom("/")


def open_zoom(_alias):
    key = list(_alias)[0]
    print()
    link = _alias[key]
    webbrowser.open(link)
    print(" Waiting for browser to open", end="")
    launch_zoom("/")


def launch_zoom(loading_symbol):
    try:
        x, y = pyautogui.locateCenterOnScreen(
            "Zoom-Launch-Meeting-Button.png", confidence=0.8
        )
        pyautogui.click(x, y)

    except TypeError:
        if loading_symbol == "\\":
            print("\r Waiting for browser to open   [" + loading_symbol + "]", end="")
            launch_zoom("/")
        else:
            print("\r Waiting for browser to open   [" + loading_symbol + "]", end="")
            launch_zoom("\\")


def more_option(opt):
    os.system("cls || clear")

    # Add
    if opt == 1:
        print(" Give alias for your meeting")
        alias = input(" [User] >>> ")

        print(" Now paste your meeting invite link")
        link = input(" [User] >>> ")

        meetings["meetings"].append(dict({alias: link}))

        with open("zoom.yml", "w") as f:
            yaml.dump(meetings, f)
        print(" Data is added")
        input("\n [ENTER] >>> ")
        print()

    # Remove
    elif opt == 2:
        i = 1
        print("\n Id     Alias")
        for meeting in meetings["meetings"]:
            x = meeting.keys()
            print(" " + str(i) + "." + ((5 - len(str(i))) * " "), list(x)[0])
            i += 1
        print(" Type the id number to delete")
        alias = int(input(" [User] >>> "))
        meetings["meetings"].pop(alias - 1)
        with open("zoom.yml", "w") as f:
            yaml.dump(meetings, f)
        print(" removed")
        input("\n [ENTER] >>> ")
        print()

    # Show
    elif opt == 3:
        i = 1
        print("\n Id     Alias")
        for meeting in meetings["meetings"]:
            x = meeting.keys()
            print(" " + str(i) + "." + ((5 - len(str(i))) * " "), list(x)[0])
            i += 1
        input("\n [ENTER] >>> ")
        print()

    # Attend
    elif opt == 4:
        i = 1
        print("\n Id     Alias")
        for meeting in meetings["meetings"]:
            x = meeting.keys()
            print(" " + str(i) + "." + ((5 - len(str(i))) * " "), list(x)[0])
            i += 1
        print(" Select the meeting number to start")
        alias = int(input(" [User] >>> "))
        print()
        open_zoom(meetings["meetings"][alias - 1])

    # help
    elif opt == 5:
        display_help()
        input("\n [ENTER] >>> ")
        print()
    # Exit
    elif opt == 6:
        exit()

    else:
        print(" Incorrect option")
    start()


def display_help():
    print("\n =====================================================")
    print(" To open your meeting from command line")
    print("\n\tCheck this following syntax")
    print("\tpython3 main.py [meeting_number]")
    print(" Example: python3 main.py 1")
    print(" =====================================================")
    print(" To open your meeting from gui")
    print("\n\tuse this command")
    print("\tpython3 main.py --gui")
    print(" =====================================================")
    print(" To add shortcut in windows")
    print("\n\t- Right click the opengui.bat")
    print("\t- Select Properties")
    print("\t- Click the Shortcut tab")
    print(
        """\t- Click in the Shortcut key box and 
          press a letter. For example, if 
          you press the P key,the key combination to 
          run this shortcut is `CTRL+ALT+P`"""
    )
    print(" =====================================================\n")


def start():
    print("==================")
    print("1. Add meeting")
    print("2. Remove meeting")
    print("3. Show meeting")
    print("4. Attend meeting")
    print("5. Shortcut")
    print("6. Exit")
    print("==================")

    try:
        opt = int(input("[User] >>> "))
    except ValueError:
        print("Incorrect option")
        start
    more_option(opt)


def gui():
    window_main = tkinter.Tk(className="Zoom Auto Launcher")
    tkinter.Label(text="Select your meeting to open").pack()
    for meeting in meetings["meetings"]:
        x = meeting.keys()
        tkinter.Button(
            window_main,
            text=list(x)[0],
            height="2",
            width="80",
            command=lambda link=meeting[list(x)[0]]: open_zoom_link(link),
        ).pack()
    window_main.mainloop()


try:
    if __name__ == "__main__":

        try:
            with open("zoom.yml", "r") as f:
                meetings = yaml.load(f, Loader=yaml.FullLoader)
        except FileNotFoundError:
            print("Give alias for your meeting")
            alias = input("[User] >>> ")

            print("Now paste your meeting invite link")
            link = input("[User] >>> ")

            meetings["meetings"].append(dict({alias: link}))

            with open("zoom.yml", "w") as f:
                yaml.dump(meetings, f)
            open_zoom_link(link)

        if len(sys.argv) == 1:
            start()
        else:
            arg1 = sys.argv[1]
            if re.match(r"[0-9]*", arg1).group():
                i = int(arg1)
                print()
                try:
                    open_zoom(meetings["meetings"][i - 1])
                except IndexError:
                    print("There is no data on that number")
                    print("Press ENTER to get the menu. To exit press CTRL+C")
                    start()
            elif arg1.lower() == "--gui":
                print("Opening gui")
                gui()
            elif arg1.lower() == "--version" or arg1.lower() == "-v":
                print("Version: 1.0.1")
            else:
                display_help()

except KeyboardInterrupt:
    print("\n\rExited Successfully")
