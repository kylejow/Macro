#https://github.com/asweigart/pyautogui
import os

from position import getPoints
import input
from win32api import Sleep


def simpleClicks():
    #sequence of 1ms clicks
    macro = []
    points = getPoints()
    for point in points:
        macro.append(input.mouseInput(1, point))
        macro.append(input.delay(100))
    return macro
def runMacro(macro):
    for item in macro:
        item.send()

test = simpleClicks()
Sleep(2000)
runMacro(test)