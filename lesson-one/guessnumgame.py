

import random
minumum = int(input("What is your lowest value: "))
maximum = int(input("What is yourgreatest value: "))
tries = int(input("How many tries would you like to give yourself: "))
guess = int(input("Make a guess: "))
correct = random.randint (minumum, maximum)

if guess == correct:
  break
elif guess > correct:
  print("Your number is too high!")
elif guess < correct:
  print("Your number is too low!")
if(guess==correct):
  print("The number is correct, you win!")