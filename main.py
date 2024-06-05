from character import character
from random import randint, choice
from time import sleep

char = character()

movements = [char.forward, char.backward, char.left, char.right]

def random() -> tuple[int | object]:
    action_time = randint(1, 10)
    option = choice(movements)

    return action_time, option

def main():
    while True:
        action_time, option = random()

        option()

        for x in range(action_time):
            print(f"Slept for {x + 1} seconds, have to wait {action_time} seconds.")
            sleep(1)

        char.stop(option.__name__)

if __name__ == "__main__":
    main()