import pandas as pd

# Step 1: Create a Series from a list
def create_series():
    data = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    series = pd.Series(data)
    return series

# Step 2: Save the Series to a CSV file
def save_series(series, filename):
    series.to_csv(filename, header=False, index=False)

# Step 3: Load the Series from a CSV file
def load_series(filename):
    # Read the CSV as a Series directly
    return pd.read_csv(filename, header=None)

# Step 4: Prompt user to access an element by its index
def access_element(series):
    try:
        index = int(input(f"Enter an index (0 to {len(series) - 1}): "))
        if 0 <= index < len(series):
            print(f"Element at index {index}: {series.iloc[index]}")
        else:
            print("Index out of range.")
    except ValueError:
        print("Invalid input! Please enter a number.")

# Main program
if __name__ == "__main__":
    # Create and save the series
    filename = "series_data.csv"
    series = create_series()
    save_series(series, filename)

    # Load and access the series
    loaded_series = load_series(filename)
    print("Loaded Series:")
    print(loaded_series)
    
    # Prompt user to access an element
    access_element(loaded_series)
