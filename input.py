import pyautogui
from win32api import Sleep


class input:
    def __init__(self, duration):
        self.duration = duration


class mouseInput(input):
    def __init__(self, duration, point):
        super().__init__(duration)
        self.point = point
    def send(self):
        pyautogui.mouseDown(self.point)
        Sleep(self.duration)
        pyautogui.mouseUp()



class keyboardInput(input):
    def __init__(self, duration, key):
        super().__init__(duration)
        self.key = key
