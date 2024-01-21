from random import *
from math import *
def enter():
    print("press enter to exit")
    input()
    exit()

def explain():
    print("next time, try to enter the number next to the operation ok?")
    enter()

print("""
select a game:
(1) guess the number (hints)
(2) guess the number (no hints)""")
game: str = input()
if game == "1":
    secretNumber = randint(1, 10)
    guess: int
    numOfGuesses = 0
    print("try to guess the secret number in 3 guesses!")
    while numOfGuesses < 3:
        print("Guess: ")
        guess = int(input())
        if guess == secretNumber:
            print("you win!")
            enter()
        elif guess < secretNumber:
            print("guess higher")
        else:
            print("guess lower")
        numOfGuesses += 1
    else:
        print("you lose")
        enter()
elif game == "2":
    secretNumber = randint(1, 10)
    guess: int
    numOfGuesses = 0
    print("try to guess the secret number in 5 guesses!")
    while numOfGuesses < 5:
        print("Guess: ")
        guess = int(input())
        if guess == secretNumber:
            print("you win!")
            enter()
        numOfGuesses += 1
    else:
        print("you lose")
        enter()
else:
    explain()