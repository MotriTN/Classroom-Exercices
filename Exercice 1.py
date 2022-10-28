# Guess the number in 5 times
# Setup
from random import*
N = randint(1, 30)
i = 0
# Code
P = int(input("Guess a number between 1 and 30: "))
while i < 5:
    if N == P:
        print("You Won!")
        break
    elif N < P:
        i = i + 1
        print("Go Less!")
        P = int(input("Guess a number between 1 and 30: "))
        continue
    else:
        i = i + 1
        print("Go More!")
        P = int(input("Guess a number between 1 and 30: "))
        continue
else:
    print("You Lost :(", "The Number was:", N)
