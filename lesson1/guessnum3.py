import random
number = random.randint(1, 10)

player_name = input("Hello, What's your name?")
number_of_guesses = 0
print('Hello '+ player_name+ ' Can you Guess a number between 1 and 10, you get 4 guesses!:')

while number_of_guesses < 4:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('The number is too low')
    if guess > number:
        print('The number is too high')
    if guess == number:
        break
if guess == number:
    print('You guessed the number in ' + str(number_of_guesses) + ' tries! GAME OVER!')
else:
    print('You did not guess the number, The number was ' + str(number))