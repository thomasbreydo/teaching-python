import random

target = random.randint(1, 10)
print("I'm thinking of a number between 1 and 10.")

while True:
    guess = int(input("What's your guess? "))
    if target == guess:
        print("Yep!")
        break
    if target > guess:
        print("Too low")
    if target < guess:
        print("Too high")
