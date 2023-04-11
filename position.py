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
run = threading.Thread(target=interrupt)
run.start()
os.system('clear')

print("Click to save positions\nEsc to exit\n")
points = []

while(not stop):
    x, y = pyautogui.position()
    if((GetKeyState(0x01) & 0x80) != 0):
        points.append([x, y])
        while((GetKeyState(0x01) & 0x80)):
            continue
    positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4) + '        '
    print(positionStr, end = '\r')

os.system('clear')
run.join()
for i, point in enumerate(points, 1):
    print(str(i) + '. ' + str(point[0]) + ', ' + str(point[1]))