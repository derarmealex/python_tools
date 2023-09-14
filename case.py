x = 10
match x:
    case 10:
        print("Začátek bloku pro hodnotu 10.")
        print("x je rovno 10. ")
        print("Konec bloku pro hodnotu 10. Zde dojde k opuštění match.")
    case 20:
        print("x je rovno 20.")
    case 30:
        print("x je rovno 30.")
    case _:
        print("x má jinou hodnotu.")
