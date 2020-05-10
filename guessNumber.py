#!/bin/python3

#
# Ramkrushna Bolewar
#
# Guess the number game
#

import random

# print("Hello, What's your name? ", end="")
name = input("Hello, whats your name? : ")

print("Hello " + name + ", I am thinking of number between 1 and 20. Can you guess? ")

guessNum = random.randint(1, 20)

i = 1
while i <= 5:
    num = int(input("Take a guess: "))
    if num < guessNum:
        print("Your guess is low. " + str(5 - i) + " attempts left.")
    elif num > guessNum:
        print("Your guess is high. " + str(5 - i) + "attempts left.")
    else:
        print("Congrats " + name + "! You guessed it in " + str(i) + "th attempt.")
        break
        
    i += 1

if guessNum != num:
    print("Attempts exhuasted!")
