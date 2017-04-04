'''
Guess My Number:
Overview:
The computer randomly generates a number. The user inputs a number, and the
computer will tell you if you are too high, or too low. Then you will get to
keep guessing until you guess the number.
What you will be Using:
Random, Integers, Input/Output, Print, While (Loop), If/Elif/Else
'''
import random

random = random.randint(1, 100)
userInput = int(input("Please enter a number between 1 and 100: "))

while (random != userInput):
    if (random > userInput):
        userInput = int(input("You're too low. Please try again! "))
    else:
        userInput = int(input("You're too high. Please try again! "))

print("Yaaay!!! you guessed it: ", random)
