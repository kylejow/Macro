#https://github.com/asweigart/pyautogui
from position import getPoints

points = getPoints()

for i, point in enumerate(points, 1):
    print(str(i) + '. ' + str(point.x) + ', ' + str(point.y))
