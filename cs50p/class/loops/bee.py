WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GRAPHIC": 7}

def main():
    print("Welcome to Spelling Bee!")
    print("Your letters are: A I P C R H G")

    while len(WORDS) > 0:
        print(f"{len(WORDS)} Words left!")
        guess = input("Guess a word: ")

        # TODO: Check if guess in dictionary
        if guess == "GRAPHIC":
            WORDS.clear()
            break
        if guess in WORDS.keys():
            points = WORDS.pop(guess)
            print(f"Congrats You've scored {points} points")

    print("That's the game")
main()