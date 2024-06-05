import pyautogui
from settings import settings

class character:
    def __init__(self) -> None:
        self.bindings = settings.bindings().getBindings()

    def forward(self) -> bool:
        try:
            pyautogui.keyDown(self.bindings["forward"])
            return True
        except pyautogui.PyAutoGUIException:
            return False
    
    def backward(self) -> bool:
        try:
            pyautogui.keyDown(self.bindings["backward"])
            return True
        except pyautogui.PyAutoGUIException:
            return False
    
    def left(self) -> bool:
        try:
            pyautogui.keyDown(self.bindings["left"])
            return True
        except pyautogui.PyAutoGUIException:
            return False
        
    def right(self) -> bool:
        try:
            pyautogui.keyDown(self.bindings["right"])
            return True
        except pyautogui.PyAutoGUIException:
            return False
    
    def stop(self, movement: str) -> bool:
        try:
            pyautogui.keyUp(movement)
            return True
        except pyautogui.PyAutoGUIException:
            return False