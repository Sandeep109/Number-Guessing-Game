import random


Number = random.randint(1,9)
num = str(Number)

chances = 4

def checker():

    global chances

    text = input("Enter your guess :- ")

    if text == num:
        print("Supperb!! You guessed the number!!")

    elif text > num:
        print("The Guess was too high , pls guess a number lower than "+text)
        if chances > 0:
            chances = chances - 1
            rechecker()

    elif text < num:
        print("The Guess was too low , pls guess a number higher than "+text)
        if chances > 0:
            chances = chances - 1
            rechecker()

def rechecker():

    global chances

    text = input("Enter your guess :- ")

    if text == num:
        print("Supperb!! You guessed the number!!")

    elif text > num:
        print("The Guess was too high , pls guess a number lower than "+text)
        if chances > 0:
            chances = chances - 1
            checker()

    elif text < num:
        print("The Guess was too low , pls guess a number higher than "+text)
        if chances > 0:
            chances = chances - 1
            checker()

checker()

if chances == 0:
    print("You don't have enough chances Pls try again")