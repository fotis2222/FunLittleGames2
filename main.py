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
(2) guess the number (no hints)
(3) [WIP] dice roller""")
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
elif game == "3":
    userRoll = 0
    enemyRoll = 0
    userScore = 0
    enemyScore = 0
    while enemyScore < 3 and userScore < 3:
        print("press enter to roll")
        input()
        userRoll = randint(1, 6)
        enemyRoll = randint(1, 6)
        print(f"you rolled a {userRoll}")
        print(f"enemy rolled a {enemyRoll}")
        if userRoll > enemyRoll:
            userScore += 1
            print("you win the round")
            print(f"your score: {userScore}, enemy's score: {enemyScore}")
        elif userRoll < enemyRoll:
            enemyScore += 1
            print("you lose the round")
            print(f"your score: {userScore}, enemy's score: {enemyScore}")
    if userScore == 3:
        print("you win the game!")
        enter()
    elif enemyScore == 3:
        print("you lose the game")
        enter()
else:
    explain()