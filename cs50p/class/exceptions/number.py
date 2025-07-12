try:
    x = int(input("What's X? "))
except ValueError:
    print("X is not an Integer") # Handling Error
else:
    print(f"X is {x}") # Only Executes if there is not an Exception
