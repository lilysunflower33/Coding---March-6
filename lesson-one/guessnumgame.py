

import random
minumum = int(input("\nWhat is your lowest value: "))
maximum = int(input("\n\nWhat is your greatest value: "))
tries = int(input("\n\nHow many tries would you like to give yourself: "))
guess = int(input("\n\nMake a guess: "))
correct = random.randint (minumum, maximum)

for x in range(tries):
  if guess == correct:
    break
  elif guess > correct:
    print("This integer is too high, try again!")
  elif guess < correct:
    print("This integer is too low, try again!")
  if guess == correct:
    print("This integer is correct, you win!")
  if guess!=correct:
    print("You loose, the correct integer was",correct,"!")