def main():
    x = get_int()
    print(f"X is {x}") # Only Executes if there is not an Exception
def get_int():
    while True:
        try:
            x = int(input("What's X? "))
        except ValueError:
            print("X is not an Integer") # Handling Error
        else:
            break
    return x

main()

