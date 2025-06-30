def main():
    results = ["Mario", "Luigi"]
    names = ["Daniel", "Santos", "Sebas"]

    # List Methods
    results.append("Peach")
    results.append("Pricess")
    results.remove("Pricess")
    results.extend(["Bowser", "Donkey Kong Jr."])
    results.insert(0, "Toad")

    # for name in range(len(names)):
       # results.insert(name, names[name])

    print(results)
main()