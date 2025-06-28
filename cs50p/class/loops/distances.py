distances = {
    "Voyager 1": 163,
    "Voyager 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44
}

def main():
    # for distance in distances.key():
    # for distance in distances.values():
    for distance in distances:
        print(distance, distances[distance], sep=" - ")

    for distance in distances.values():
        print(f"{distance} AU is {convert_to_meter(distance)} m");

# Convert Away from earth to meters
def convert_to_meter(au):
    return au * 149597870700
main()