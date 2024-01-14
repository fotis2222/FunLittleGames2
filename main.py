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
(1) guess the number (hints)""")
game: str = input()
if game == "1":
    pass
else:
    explain()