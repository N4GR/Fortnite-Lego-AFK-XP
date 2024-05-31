import character
from tqdm import tqdm
import time
import random

movements = [character.move.left, character.move.right, character.move.forward, character.move.backward, character.move.nothing, character.move.punch]

def single_movement():
    x = input("Begin the script by pressing enter.")
    previous_movement = ""

    while True:
        while True: # Ensures the movement previous movement isn't the same as the new one
            multi = random.randint(1, 2)

            if multi == 2:
                random_key = [random.choice(movements), random.choice(movements)]

                for key in random_key:
                    key()
                
                for x in tqdm(range(random.randint(3, 10))):
                    time.sleep(1)
                    if random.randint(1, 10) == 1:
                        character.move.jump()
                
                for key in random_key:
                    character.move.stop(key.__name__)

            else:
                random_key = random.choice(movements)
                if random_key.__name__ != previous_movement:
                    previous_movement = random_key.__name__
                    break

                random_key()

                for x in tqdm(range(random.randint(3, 10))):
                    time.sleep(1)
                    if random.randint(1, 10) == 1:
                        character.move.jump()
                
                character.move.stop(random_key.__name__)

single_movement()