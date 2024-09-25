import pandas as pd

# Step 1: Create a DataFrame from lists
def create_dataframe():
    data = {
        'Fruit': ['apple', 'banana', 'cherry', 'date', 'elderberry'],
        'Color': ['red', 'yellow', 'red', 'brown', 'purple'],
        'Weight': [150, 120, 15, 30, 5]
    }
    df = pd.DataFrame(data)
    return df

# Step 2: Save the DataFrame to a CSV file
def save_dataframe(df, filename):
    df.to_csv(filename, index=False)

# Step 3: Load the DataFrame from a CSV file
def load_dataframe(filename):
    return pd.read_csv(filename)

# Step 4: Prompt user to access a row by its index
def access_row(df):
    try:
        index = int(input(f"Enter an index (0 to {len(df) - 1}): "))
        if 0 <= index < len(df):
            print(f"Row at index {index}:")
            print(df.iloc[index])
        else:
            print("Index out of range.")
    except ValueError:
        print("Invalid input! Please enter a number.")

# Main program
if __name__ == "__main__":
    # Create and save the DataFrame
    filename = "dataframe_data.csv"
    df = create_dataframe()
    save_dataframe(df, filename)

    # Load and access the DataFrame
    loaded_df = load_dataframe(filename)
    print("Loaded DataFrame:")
    print(loaded_df)
    
    # Prompt user to access a row
    access_row(loaded_df)
