# This program is produced by BlueGa, BlueCloudTeam
# Version: 0.0.6
# Update date: 2023.8.1
# No handling!


import pyautogui as gui
import time
import sys

gui.size()
gui.position()
gui.FAILSAFE = True

# ------------------------------------------------↓Update the content↓------------------------------------------------------------
with open("UpdateContent.txt", "w", encoding="utf-8") as UC:
    UC.write("Minecraft script update\nversion: 0.0.6\nUpdate the content:\n1.Add precautions;2.Optimizer makes use\nNo handling!\nMade By BlueCloudTeam")

# ----------------------------------------------↓body↓---------------------------------------------------------------------


def start():  # Menu section
    print("""
        minecraft scripts
    1.open script   2.open tutorial
    3.Contact us    4.Version details
    5.synopsis      6.Notes
    0.exit     0.exit
    
    Made By BlueCloudTeam
    """)
    StartQ1 = input("select:")
    if StartQ1 == "1":
        minecraftscript()
    elif StartQ1 == "2":
        cos()
    elif StartQ1 == "3":
        print("Contact us, please join the QQ group:906798648(Team Groups)")
	print("Or send an email to shiftbluega@qq.com with the intention")
        start()
    elif StartQ1 == "4":
        print("This version is 0.0.6, update date: 2023.8.1")
        print("Made By BlueCloudTeam")
        start()
    elif StartQ1 == "5":
        rtp()
    elif StartQ1 == "6":
        notes()
    elif StartQ1 == "0":
        sys.exit(0)
    else:
        start()


def minecraftscript():  # Script section
    print("""
        minecraft script
    1.Automatic digging of stones
    2.Automated mining (straight mines)
    3.Automatic Monster Fighting (Brush Tower)
    0.back
    """)
    ScriptQ1 = input("select:")
    if ScriptQ1 == "1":
        matictime = int(input("Duration (seconds):"))
        time.sleep(5)
        gui.mouseDown(button="left")
        time.sleep(matictime)
        gui.mouseUp(button="left")
        print("End of run! Welcome to visit next time!")
        start()
    elif ScriptQ1 == "2":
        autominingtime = int(input("Duration (seconds):"))
        time.sleep(5)
        gui.mouseDown(button="left")
        gui.keyDown("w")
        time.sleep(autominingtime)
        gui.mouseUp(button="left")
        gui.keyUp("w")
        print("End of run! Welcome to visit next time!")
        start()
    elif ScriptQ1 == "3":
        autokillzombiletime = int(input("Number of durations:"))
        time.sleep(5)
        for autokillzombile in range(autokillzombiletime):
            gui.mouseDown(button="left")
            gui.mouseUp(button="left")
            time.sleep(1.2)
        time.sleep(1)
        print("End of run! Welcome to visit next time!")
        start()
    elif ScriptQ1 == "0":
        print("Returned!")
        start()
    else:
        minecraftscript()


def cos():  # Tutorial section
    print("""
        minecraft scripting tutorials
    1.Automatic digging of stones
    2.Automated mining (straight mines)
    3.Automatic Monster Fighting (Brush Tower)
    0.back
    """)
    cosQ1 = input("select:")
    if cosQ1 == "1":
        print("Automatic stone digging tutorial: 1. Hold the manuscript in your hand; 2. Start the procedure; 3. Return to the game within 5 seconds
Inside; 4. Align the stone in a short time after starting")
        time.sleep(3)
        cos()
    elif cosQ1 == "2":
        print(
            "Auto Mining (Straight Track) Tutorial: 1. Open F3, align the front sight with the gap between the two blocks up the pixel and make sure The front sight is 90° (0°, 90°, -90°, 180°) 1. In a two-block high straight tunnel; 2. Hold the manuscript in your hand; 3. Start the program; 4.Return to the game within 5 seconds")
        time.sleep(5)
        cos()
    elif cosQ1 == "3":
        print("Automatic monster fighting  tutorial: 1. Hold the weapon in your hand; 2. Start the procedure; 3. Return to the game within 5 seconds; 4.After starting, aim at the center of the monster landing point for a short time")
        time.sleep(2)
        cos()
    elif cosQ1 == "0":
        print("Returned!")
        start()
    else:
        cos()


def rtp():  # 认识程序部分
    print(
        "This program is specially made for Minecraft, this program will greatly help us solve the simple and difficult problems encountered when playing Minecraft

Tedious things such as digging stones, brushing monsters, etc.! And this program does not affect other players' games, which is very suitable for playing survival save or server

Server. The current version of this program is 0.0.6! Tips: If you are playing server, you must pay attention to the server rules! ")
    print("""
    Made By BlueCloudTeam
    """)
    time.sleep(3)
    start()


def notes():
    print("The Minecraft version of the program is available:1.9-1.20.2")
    print("If you encounter problems, you can give feedback, how to feedback see contact us")
    print("Thanks for the support uwu")
    time.sleep(3)
    start()


# ------------------------------------------------↓start↓------------------------------------------------------------

start()



