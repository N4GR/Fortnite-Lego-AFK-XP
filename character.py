import pyautogui

class move():
    '''
    Move class used to interact with the player.
    '''
    def left() -> None:
        '''
        Moves the player left.
        '''
        pyautogui.keyDown("a")
        
    def right() -> None:
        '''
        Moves the player right.
        '''
        pyautogui.keyDown("d")
    
    def forward() -> None:
        '''
        Moves the player foward.
        '''
        pyautogui.keyDown("w")

    def backward() -> None:
        '''
        Moves the player backward.
        '''
        pyautogui.keyDown("s")

    def jump() -> None:
        '''
        Makes the player jump.
        '''
        pyautogui.press("space")

    def nothing():
        '''
        Makes the character do nothing.
        '''

    
    def stop(movement: str) -> None:
        '''
        Stops the player from moving using a given movement.

        movement: str (The direction to stop)

        Example: stop("right")
        '''

        if movement == "left": pyautogui.keyUp("a")
        elif movement == "right": pyautogui.keyUp("d")
        elif movement == "forward": pyautogui.keyUp("w")
        elif movement == "backward": pyautogui.keyUp("s")