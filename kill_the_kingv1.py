import random
import time
import os
import pygame

#### Functions #####

# Creates start menu
def menu():
    w = 65
    os.system('cls' if os.name == 'nt' else 'clear') #clears screen
    print("+"*(w+2))
    for i in range(18):
        if i == 2:
            a = len("CONSOLE GAME: KILL THE KING")
            print("+", " "*(int((w-2-a)/2-1)), "CONSOLE GAME: KILL THE KING", " "*(int((w-2-a)/2-1)), "+")
        elif i == 5:
            a = len("by Mr Claassens")
            print("+", " "*(int((w-a)/2-2)), "by Mr Claassens", " "*(int((w-a)/2-2)), "+")
        elif i == 10:
            a = len("Instructions:")
            print("+", " "*(int((w-2-a)/2-2)), "Instructions:", " "*(int((w-a)/2-1)), "+")
        elif i == 11:
            a = len("You are an assassin that is known for killing royalty.") 
            print("+", " "*(int((w-2-a)/2-1)), "You are an assassin that is known for killing royalty.", " "*(int((w-2-a)/2)), "+")
        elif i == 12:
            a = len("First find the king then poison him!")
            print("+", " "*(int((w-2-a)/2-1)), "First find the king then poison him!", " "*(int((w-2-a)/2)), "+")
        elif i == 17:
            print("+"*(w+2))
        else:
            print("+", " "*(w-2), "+")
        
    for i in range(2):
            print(" ")
        
    print("Do you accept your mission?")
    
    menu_choice = input("Enter y/n: \n\n> ").lower()
    while menu_choice not in ["y", "yes"]:
        if menu_choice not in ["n", "no"]:
            print("Please play the game...")
        else:
            print("Incorrect input. Try again. \n")
        menu_choice = input("Enter y/n: \n\n> ")
    if menu_choice in ["y", "yes"]:
        return True
    else:
        return False
    
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
        print(f"\nTime left: {round(timer - (current_time - start_time),1)}")
        if current_time - start_time > timer:
            print("\nYou took too long the King has slipped from your reach.")
            math_active == False
            break
        print(f"You need to add {target} drops to make poison!")
        print(f"Drops added: {total}")
        print("\n")
            
        # Validate the amount of drops a player can add to only be 3, 5 or 7
        choice = int(input("Add 3, 5 or 7 drops: "))
        if current_time - start_time >timer:
            print("\n You took too long the King has slipped from your reach. You are arrested and hung!")
            math_active == False
            break
        while choice != 3 and choice != 5 and choice != 7:
            choice = int(input("Try again! Add 3, 5 or 7 drops: "))
            
        total += choice
        if total == target:
            print("You've poisoned the King! \nOn to the next kingdom!")
            timer_active = False
            game_active = False
            time.sleep(5)
            os.system('cls' if os.name == 'nt' else 'clear') #clears screen
            return True
            break
        elif total > target:
            print("You've added too much and the smell of poison was obvious! \nYou've been arrested and hung...")
            timer_active = False
            game_active = False
            time.sleep(5)
            os.system('cls' if os.name == 'nt' else 'clear')
            return False
        else:
            print("Still more drops to add...")
            time.sleep(1)
            print("="*47)
            print("\n"*50)
            os.system('cls' if os.name == 'nt' else 'clear')

def guess_pos():
    global guess
    guess = int(input("Which position is the King? \nEnter spot (1-6): "))
    if spots[guess-1] == "King":
        return True
    else:
        return False
 
### ASCII Graphic endings ###

def dog():
    print("""
 __.     ._.
oxx)}____//.
 `_/      ).
 (_(_/-(_/.
    
  You're a monster... why kill a puppy?""")

def queen():
    print("""
      ___
    .|v v|. 
   .(_)_(_).
    .(x x).
    ._ ^ _.
 -- / ' ' \--.
  ./   "   \.
 ./_________\.
 .|         |.
 .(_________).
   .U.    .U.
    
  She was simply trying to have a good evening... Happy?""")
    
def jester():
     print("""
     ._  _  _.
    .(_)(_)(_).  . .
   ./  \ | /  \ .O.
  .|____\|/____|/.
    .( >  < )  /.
     .|  ^  | /.
    .o '- -' O.
    ./ /|/ \ ||.
     .|_|  |_|.
     ./_/  \_\.
    
  I guess he told his last joke...""")
def guard():
    print("""
     . _____.
     .[_____].
      .(X X).
      ._|v|_.  .^.
     ./| _ |\ .| |.
    .|_|   |_|.| |.
      .|___|. .| |.
     ./|   |\..| |.
    ./_|___|_\_| |_.
     .|_| |_|  -|-.
    
  He has two kids at home... You feel good about yourself?""")
def chef():
    print("""
      ._____.
     .(     ).
    .(_______).
     .( X X ).
      .\ - /.
      ._| |_  __.
     ./ | | \/  \.
    .|  |_|  |  /.
    .|_______|--.
     .|_| |_|.
     ./_/ \_\.
    
  After a hard day of slaving away in the kitchen... what bad luck...""")

def hung():
    print("""
    ._______...
    .|/     .|.
    .|     .(x).
    .|     .\|/.
    .|      .|.
    .|     ./ \.
    .|
 .___|___.
./       \.
/_________\.
    
  Your story ends here... Monarchs rejoice and the rabble consider what could have been...""")

### Setting Background Music ###
pygame.mixer.init()
pygame.mixer.music.load("ChillMenu_Loopable.wav")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

#### Game Loop ######
game_active = True
total_score = 0
court_diff = 0
math_limit = 25
timer = 15
 
menu()
time.sleep(2)

pygame.mixer.music.load("SeeingDouble_Loopable.wav")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

os.system('cls' if os.name == 'nt' else 'clear')
while game_active == True:
    
    # Print a new random order to the court    
    for i in range(3):
        spots = court_shuffle()
        time.sleep(4-court_diff)
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
            print("\n")
            print("="*30)
            print("Game over!")
            print(f"Your final score is {total_score}")
            print("="*30)
            game_active = False
            ending = "hung"
            
        if court_diff < 4:
            court_diff += 0.5
        if math_limit > 100:
            math_limit += 15
        if timer > 5:
            timer -= 2
    else:
        print("\n")
        print("="*30)
        print(f"Whoops... You poisoned the {spots[guess-1]}")
        print("Game over!")
        print(f"Your final score is {total_score}")
        print("="*30)
        if spots[guess-1] == "Dog":
            ending = "dog"
        elif spots[guess-1] == "Queen":
            ending = "queen"
        elif spots[guess-1] == "Jester":
            ending = "jester"
        elif spots[guess-1] == "Chef":
            ending = "chef"
        elif spots[guess-1] == "Guard":
            ending = "guard"
        game_active = False
        
time.sleep(3)

os.system('cls' if os.name == 'nt' else 'clear')
pygame.mixer.music.load("you_died.wav")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)


if ending == "dog":
    dog()
elif ending == "queen":
    queen()
elif ending == "jester":
    jester()
elif ending == "chef":
    chef()
elif ending == "guard":
    guard()
elif ending == "hung":
    hung()

time.sleep(7)
pygame.mixer.music.stop()






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
