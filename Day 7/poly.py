class Calculator:
    # Method to add numbers, demonstrates overloading by checking arguments
    def add(self, a=None, b=None, c=None):
        if a is not None and b is not None and c is not None:
            return a + b + c  # If all three arguments are provided
        elif a is not None and b is not None:
            return a + b  # If two arguments are provided
        else:
            return a

# Create an instance of Calculator
calc = Calculator()

# Demonstrating polymorphism by calling 'add' with different numbers of arguments
print(calc.add(1, 2))         # Outputs: 3
print(calc.add(1, 2, 3))      # Outputs: 6
print(calc.add(1))            # Outputs: 1
