#https://codeloop.org/python-gui-automation-getting-mouse-position/

import pyautogui
import keyboard
import threading
import os
from win32api import GetKeyState

stop = False
def interrupt():
    keyboard.wait('esc')
    global stop
    stop = True

def getPoints():
    run = threading.Thread(target=interrupt)
    run.start()
    os.system('cls')

    print("Click to save positions\nEsc to exit\n")
    points = []

    while(not stop):
        point = pyautogui.position()
        if((GetKeyState(0x01) & 0x80) != 0):
            points.append(point)
            while((GetKeyState(0x01) & 0x80)):
                continue
        positionStr = 'X: ' + str(point.x).rjust(4) + ' Y: ' + str(point.y).rjust(4) + '        '
        print(positionStr, end = '\r')

    os.system('cls')
    run.join()
    return points
