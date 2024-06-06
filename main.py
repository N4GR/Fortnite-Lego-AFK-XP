from character import character
from random import randint, choice
from time import sleep
from log import log

class main:
    def __init__(self) -> None:
        self.player = character()
    
    def movement(self) -> list[object]:
        movements = [self.player.forward, self.player.backward, self.player.left, self.player.right]

        return movements

    def randomAction(self) -> tuple[int | list[object]]:
        illegal_actions = [
            ["left", "right"],
            ["right", "left"],
            ["forward", "backward"],
            ["backward", "forward"],
            ["left", "left"],
            ["right", "right"],
            ["forward", "forward"],
            ["backward", "backward"]
            ]

        action_time = randint(1, 10)

        while True:
            actions = []
            for x in range(randint(1, 2)):
                actions.append(choice(self.movement()))

            stuff = []
            for action in actions:
                stuff.append(action.__name__)

            if stuff in illegal_actions:
                continue
            else:
                break
        
        print(log().note(f"Randomly chosen the aciton/s: {(stuff[0], stuff[1]) if len(stuff) == 2 else stuff[0]}..."))

        return action_time, actions

    def start(self) -> None:
        char = character()

        times_ran = 1

        while True:
            print(log().note(f"Ran {times_ran} time/s..."))
            complete_actions = []
            action_time, actions = self.randomAction()

            for action in actions:
                print(log().note(f"Pressing the action: {action.__name__}..."))
                action()
                complete_actions.append(action)

            print(log().note(f"Waiting {action_time}s until next action..."))

            for x in range(action_time):
                roll = randint(1, 20)
                if roll == 1:
                    char.jump()
                elif roll == 2:
                    char.punch()

                sleep(1)
                print(log().note(f"Waiting {x + 1}/{action_time}..."))

            for action in complete_actions:
                self.player.stop(action.__name__)
                print(log().note(f"Stopping {action.__name__}..."))
            
            print(log().success(f"Successfully completed actions, going again...\n"))

            times_ran += 1

if __name__ == "__main__":
    start_time = 5

    print(log().note(f"Program will begin in {start_time}s..."))
    for x in range(start_time):
        sleep(1)
        print(log().note(f"{x + 1}/{start_time}s..."))

    print(log().note(f"Beginning now...\n"))

    main().start()