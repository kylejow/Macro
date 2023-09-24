#https://github.com/asweigart/pyautogui
import os

from position import getPoints
import inputTypes
from win32api import Sleep


def simpleClicks(delay):
    #sequence of 1ms clicks separated by delay in ms
    macro = []
    points = getPoints()
    for point in points:
        macro.append(inputTypes.mouseInput(1, point))
        macro.append(inputTypes.delay(delay))
    return macro
def runMacro(macro):
    for item in macro:
        item.send()

def custom():
    macro = []
    action = 0
    while action != '6':
        os.system('cls')
        action = input("1. Delay\n2. Mouse Down\n3. Mouse Up\n4. Key Down\n5. Key Up\n6. Save and Exit\n")
        os.system('cls')
        if action == '1':
            delay = input("Enter Delay in ms: ")
            macro.append(inputTypes.delay(int(delay)))
        elif action == '2':
            macro.append(inputTypes.mouseInputDown)
        elif action == '3':
            macro.append(inputTypes.mouseInputUp)
        elif action == '4':
            key = input("Enter Key: ")
            macro.append(inputTypes.keyboardInputDown(1, key))
        elif action == '5':
            key = input("Enter Key: ")
            macro.append(inputTypes.keyboardInputUp(1, key))
        else:
            continue
    return macro
