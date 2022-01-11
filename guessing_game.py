import random
import time
print('Lets play a guessing game!')

player_name = input('What is your name?\n')
print(f"{player_name}, I'm thinking of a number between 1 and 100.")

actual_number = random.randint(1,100)
amount_of_tries = 0

while(True):
    player_guess = int(input('Guess a number!'))
    amount_of_tries += 1
    if (player_guess > actual_number):
        time.sleep(.5)
        print('Your guess is too high. Try again.')
    elif(player_guess < actual_number):
        time.sleep(.5)
        print('Your guess is too low. Try again.')
    else:
        time.sleep(.5)
        print(f"Nice guess {player_name}! {actual_number} was my number! You got it in {amount_of_tries} attempts!")
        break