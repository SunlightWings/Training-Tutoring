# Calculator Game:

def calculator(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero!"
    else:
        return "Invalid operation! Please use +, -, *, or /"

# Function call
if __name__ == "__main__":
    # Example inputs for the game
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    result = calculator(a, b, operation)
    print(f"The result is: {result}")
