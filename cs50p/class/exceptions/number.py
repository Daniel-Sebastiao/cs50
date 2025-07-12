try:
    x = int(input("What's X? "))
except ValueError:
    print("X is not an Integer") # Handling Error

#
print(f"X is {x}")