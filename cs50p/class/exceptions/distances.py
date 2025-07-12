distances = {
    "Voyager 1": "163",
    "Voyager 2": "136",
    "Pioneer 10": "80 AU",
    "New Horizons": "58",
    "Pioneer 11": "44 AU",
}

def main():
    spacecraft = input("Enter a Spacecraft: ").lower().title()
    try:
        print(convert(int(distances[spacecraft])))
    except KeyError:
        print(f"'{spacecraft}' is not existent")
    except ValueError:
        print(f"'{distances[spacecraft]}' can not be converted")



def convert(au):
    return au * 149597870700

main()

