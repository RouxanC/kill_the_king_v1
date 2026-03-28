import random
import time
import os

#### Functions #####

# Creates a list called spots with the King, Queen, etc. (NPCs) in a random order -- return the list
def shuffle():
    queen = random.randint(1,6)

    jester = random.randint(1,6)
    while jester == queen:
        jester = random.randint(1,6)

    king = random.randint(1,6)
    while king == queen or king == jester:
        king = random.randint(1,6)

    chef = random.randint(1,6)
    while chef == queen or chef == jester or chef == king:
        chef = random.randint(1,6)

    dog = random.randint(1,6)
    while dog == queen or dog == jester or dog == king or dog == chef:
        dog = random.randint(1,6)

    guard = random.randint(1,6)
    while guard == queen or guard == jester or guard == king or guard == dog or guard == chef:
        guard = random.randint(1,6)

    spots = [" ", " ", " ", " ", " ", " "]

    spots[queen - 1] = "Queen"
    spots[jester - 1] = "Jester"
    spots[king - 1] = "King"
    spots[chef - 1] = "Chef"
    spots[dog - 1] = "Dog"
    spots[guard - 1] = "Guard"
    return spots

# Takes the random spots list and prints it to the terminal in pretty format
def court_shuffle():
    spots = shuffle()
    print("="*15, "Court positions", "="*15)
    print("|", spots[0], "|", spots[1], "|", spots[2], "|", spots[3], "|", spots[4], "|", spots[5], "|")
    print("="*47)
    return spots

def math_prob(limit, timer):
    total = 0
    start_time = time.time()
    math_active = True

    target = random.randint(8,limit)
    while math_active == True:
        current_time = time.time()

        if current_time - start_time > timer:
            print("You took too long the King has slipped from your reach.")
            math_active == False
            break
        print(f"You need to add {target} drops to make poison!")
        print(f"Drops added: {total}")
        print("\n")

        # Validate the amount of drops a player can add to only be 3, 5 or 7
        choice = int(input("Add 3, 5 or 7 drops: "))
        if current_time - start_time > 10:
            print("You took too long the King has slipped from your reach.")
            math_active == False
            break
        while choice != 3 and choice != 5 and choice != 7:
            choice = int(input("Try again! Add 3, 5 or 7 drops: "))

        total += choice
        if total == target:
            print("win")
            timer_active = False
            game_active = False
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear') #clears screen
            return True
            break
        elif total > target:
            print("lose")
            timer_active = False
            game_active = False
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            return False
        else:
            print("Still more drops...")
            time.sleep(1)
            print("="*47)
            print("\n"*50)
            os.system('cls' if os.name == 'nt' else 'clear')

def guess_pos():
    global guess
    guess = int(input("Which position is the King? \n Enter spot (1-6): "))
    if spots[guess-1] == "King":
        return True
    else:
        return False


#### Game Loop ######
game_active = True
total_score = 0
court_diff = 0
math_limit = 25
timer = 10

while game_active == True:

    # Print a new random order to the court
    for i in range(3):
        spots = court_shuffle()
        time.sleep(5-court_diff)
        print("\n"*50)
        os.system('cls' if os.name == 'nt' else 'clear')

    if guess_pos() == False:
        game_active = False
        guess_correct = False
    else:
        print("You found the King!")
        guess_correct = True
        time.sleep(2)

    if guess_correct == True:
        math_game_outcome = math_prob(math_limit, timer)
        if math_game_outcome == True:
            total_score += 1
        else:
            game_active = False

        if court_diff < 2:
            court_diff += 0.5
        if math_limit > 100:
            math_limit += 15
    else:
        print("\n", "="*30)
        print(f"Whoops... You poisoned the {spots[guess-1]}")
        print("Game over!")
        print(f"Your final score is {total_score}")
        print("="*30)
        game_active = False










"""
Game Loop:

1. The screen displays the names of the NPCs as [King] [Jester], [Queen], etc.

2. They shuffle to different positions.

3. Wait some interval (4 sec)

4. Repeat 2 and 3 twice.

5. Clear screen.

6. The math problem comes up with time limit.

7. If problem is answered wrong or time runs out - show end screen and that they got caught.

8. If problem is correct, ask which position to poison.

9. If choice is wrong - show end screen and who they poisoned and that they got caught.

10. If choice is right restart steps 1-9 but make the interval 1s shorter and the math problem is 2s shorter.

11. If they keep passing again keep removing time until it is 1s interval and the math problem is 5s.
"""
