#https://codeloop.org/python-gui-automation-getting-mouse-position/

import pyautogui
import keyboard
import threading
import os

stop = False
def interrupt():
    keyboard.wait('esc')
    global stop
    stop = True
run = threading.Thread(target=interrupt)
run.start()
os.system('clear')

print("Esc to exit\n")
while(not stop):
    x, y = pyautogui.position()
    positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
    print(positionStr, end = '\r')

os.system('clear')
run.join()
