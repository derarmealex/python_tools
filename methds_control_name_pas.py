while True:
    user = dict(Name="Marek", Password="1234")
    n = input("Enter your username: ")
    p = input("Enter your password: ")
    if n == user.get("Name") and user.get("Password") == p:
        print("\n\tWelcome to app! You can go on...\n")
        break
    else:
        print("\n\tUsername or password isn't OK!\n")
# or
user = {'Marek': '1234'}
while True:
    n = input("Enter your username: ")
    p = input("Enter your password: ")
    if user.get(n) == p:
        print("\n\tWelcome to app! You can proceed...\n")
        break
    else:
        print("\n\tUsername or password isn't OK!\n")
