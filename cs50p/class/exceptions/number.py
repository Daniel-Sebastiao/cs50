def main():
    x = get_int()
    print(f"X is {x}") # Only Executes if there is not an Exception

def get_int():
    while True:
        try:
            return int(input("What's X? "))
        except ValueError:
            pass # Handling Error

main()

