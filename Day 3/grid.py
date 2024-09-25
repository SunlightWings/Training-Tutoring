import array
import random
import time

# Initialize a 3x3 grid with periods (.)
def create_grid():
    grid = [['.' for _ in range(3)] for _ in range(3)]
    return grid

# Display the current state of the grid
def display_grid(grid):
    for row in grid:
        print(" ".join(row))
    print()

# Randomly place the dollar symbol ($) in the grid
def place_dollar(grid):
    row = random.randint(0, 2)
    col = random.randint(0, 2)
    grid[row][col] = '$'
    return (row, col)

# Main game function
def play_game():
    grid = create_grid()
    dollar_position = place_dollar(grid)
    display_grid(grid)
    
    print("Capture the dollar ($) by entering the correct row and column within 1 second!")
    
    # Start timer
    start_time = time.time()

    while True:
        # Check if time exceeds 3 second
        if time.time() - start_time > 3:
            print("Too slow! You lose.")
            break
        
        try:
            # Get the player's input for row and column
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
            
            # Check if the input matches the dollar symbol position
            if (row, col) == dollar_position:
                print("Congratulations! You captured the dollar symbol.")
                return
            else:
                print("Wrong position! Try again quickly!")
        except ValueError:
            print("Invalid input! Please enter a valid row and column.")

    # Restart the game
    print("Restarting the game...\n")
    play_game()

# Start the game
play_game()
