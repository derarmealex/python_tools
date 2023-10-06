fruits = {"apple": 0, "banana": 0, "lemon": 0, "orange": 0}
while True:
    print("Avialable fruits:", ", ".join(fruits))
    choice = input("Choose from available fruits: ").lower().strip()
    if choice in fruits:
        print("Great, this fruit is in offer")
        fruits[choice] += 1
        while True:
            another_choice = input(
                "\nAnother fruit to choice? Press 'y'\n"
                "For seeing your basket, press 'b'\n"
                "To finish shopping press 'n'\n"
                                    ).lower().strip()
            if another_choice == "y":
                break
            elif another_choice == "b":
                print("\nHere is your basket: ", ", ".join([f"{key}: {value}" for key, value in fruits.items()]))
            elif another_choice == "n":
                print("\nSee ya again!")
                print("Here is your basket: ", ", ".join([f"{key}: {value}" for key, value in fruits.items()]))
                input("\nPress any key")
                exit()
            else:
                print("\nPress 'y', 'n' or 'b'!".upper())
    else:
        print("\nFruit is not in offer!")
