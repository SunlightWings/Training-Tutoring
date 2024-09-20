# Guessing game:

import random

def guess_the_number():
    print("Welcome to the Guess the Number Game!")
    print("I am thinking of a number between 1 and 100.")
    
    # The computer picks a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 7  # Limiting the player to 7 attempts

    # While loop to manage the game
    while attempts < max_attempts:
        try:
            guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts}: Enter your guess: "))

            if guess < 1 or guess > 100:
                print("Your guess is out of bounds! Please guess a number between 1 and 100.")
                continue

            attempts += 1

            # Checking the player's guess
            if guess < number_to_guess:
                print("Too low! Try a higher number.")
            elif guess > number_to_guess:
                print("Too high! Try a lower number.")
            else:
                print(f"\nCongratulations! You've guessed the number {number_to_guess} in {attempts} attempts!")
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    # If the player runs out of attempts, they lose the game
    if attempts == max_attempts and guess != number_to_guess:
        print(f"\nSorry! You've run out of attempts. The correct number was {number_to_guess}. Better luck next time!")

# Call the function to start the game
if __name__ == "__main__":
    guess_the_number()
