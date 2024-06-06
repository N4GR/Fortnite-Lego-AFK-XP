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
        
    def jump(self) -> bool:
        try:
            pyautogui.press(self.bindings["jump"])
            return True
        except pyautogui.PyAutoGUIException:
            return False
        
    def punch(self) -> bool:
        try:
            pyautogui.leftClick()
            return True
        except pyautogui.PyAutoGUIException:
            return False
        
    def stop(self, movement: str) -> bool:
        try:
            method = getattr(character, movement)
            binding = self.bindings[method.__name__]
            pyautogui.keyUp(binding)
            return True
        except pyautogui.PyAutoGUIException:
            return False