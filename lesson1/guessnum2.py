# guess a randomly generated number

input("Welcome to my guess the number game! \n\n Steps: \n Press 'Enter' after every input to continue. \n Input the highest number to input a range. \n Guess the number! \n\n Good Luck, Enjoy!")

from numpy import random
max = input("\n\nInput largest number: ")
randomgen = random.randint(0, max)
correctnum = randomgen
isnumbercorrect = bool(False)

while isnumbercorrect == False:
    guess = int(input("\nWhat is the number? "))
    if guess == correctnum:
        print("Your guess is correct!")
        isnumbercorrect = bool(True)
    else:
        if guess < correctnum:
                print("The number you entered is too low, try again!")
        if guess > correctnum:
                print("The number you entered is too high, try again!")

print("\n\nGame Over.\n")