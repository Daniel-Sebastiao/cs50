try:
    # Ask an Input for the User
    x = int(input("What's X? "))
    # If The value Typed in is an Integer
    print(f"X is {x}")
except ValueError:
    # Else
    print("X is not an Integer")