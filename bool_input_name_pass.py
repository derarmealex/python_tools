user = dict(Name= "Marek", Password= "1234")
while True:
    n = input("Enter your username: ")
    p = input("Enter your password: ")
    if bool(n == user.get("Name")) and bool(user.get("Password") == p) == True:
        print("Ahoj Marek vítej v aplikaci! Pokračuj...")
        break
    else:
        print("Uživatelské jméno nebo heslo nejsou v pořádku!")
#or
user = dict(Name= "Marek", Password= "1234")
while True:
    n = input("Enter your username: ")
    p = input("Enter your password: ")
    if bool((n == user.get("Name")) and bool(user.get("Password") == p)) == False:
        print("Uživatelské jméno nebo heslo nejsou v pořádku!")
    else:
        print("Ahoj Marek vítej v aplikaci! Pokračuj...")
        break
#or
user = {'Marek': '1234'}
while True:
    n = input("Enter your username: ")
    p = input("Enter your password: ")
    if user.get(n) == p:
        print("Ahoj Marek vítej v aplikaci! Pokračuj...")
        break
    else:
        print("Uživatelské jméno nebo heslo nejsou v pořádku!")
