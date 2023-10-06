x = int(input("Enter a number: "))
match x:
    case 10:
        print("x is", x)                    # x is 10
    case 20:
        print("x is", x)                    # x is 20
    case 30:
        print("x is", x)                    # x is 30
    case _:
        print("x is", x)                    # x is ...
# or
x = int(input("Enter a number: "))          # 99
match x:
    case 10: print("x is", x)               # x is 10
    case 20: print("x is", x)               # x is 20
    case 30: print("x is", x)               # x is 30
    case _: print("x is", x)                # x is 99
