def is_leap_year(year):
    if (year % 400 == 0):
        print(f"{year} is a leap year.")
    elif (year % 100 == 0):
        print(f"{year} is not a leap year.")
    elif (year % 4 == 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

# Example usage
year = int(input("Enter a year: "))
is_leap_year(year)
