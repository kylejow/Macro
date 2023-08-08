#https://github.com/asweigart/pyautogui
from position import getPoints
import input
from win32api import Sleep

points = getPoints()

for i, point in enumerate(points, 1):
    print(str(i) + '. ' + str(point.x) + ', ' + str(point.y))

Sleep(3000)
testInputs = []
testInputs.append(input.mouseInput(10, points[0]))
testInputs.append(input.keyboardInput(10, "a"))
for input in testInputs:
    input.send()