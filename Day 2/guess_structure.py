## Game:
import random

def number_guessing_game():
    # Tuple: fixed range of numbers to guess from
    number_range = (1, 100)
    
    # Dictionary: stores hints for too high or too low guesses
    hints = { 'high': 'Too high!', 'low': 'Too low!' }
    
    # Set: to track numbers the player has already guessed
    guessed_numbers = set()

    # List: player's past guesses
    past_guesses = []

    # Randomly choose the target number
    target_number = random.randint(*number_range)
    
    print(f"Guess the number between {number_range[0]} and {number_range[1]}!")
    
    while True:
        guess = int(input("Enter your guess: "))

        # If already guessed, alert the player
        if guess in guessed_numbers:
            print("You already guessed that! Try another number.")
            continue
        
        # Add guess to both the set and list
        guessed_numbers.add(guess)
        past_guesses.append(guess)
        
        # Check if the guess is correct
        if guess == target_number:
            print(f"Congratulations! You guessed it in {len(past_guesses)} tries!")
            break
        elif guess > target_number:
            print(hints['high'])
        else:
            print(hints['low'])

# Start the game
if __name__ == "__main__":
    number_guessing_game()
