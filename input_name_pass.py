user = dict(Name="Marek", Password="1234")
while True:
    n = input("Enter your username: ")
    p = input("Enter your password: ")
    if n == user.get("Name") and user.get("Password") == p:
        print("Welcome to app! You can go on...")
        break
    else:
        print("Username or password isn't OK!")
# or
user = dict(Name="Marek", Password="1234")
while True:
    n = input("Enter your username: ")
    p = input("Enter your password: ")
    if n == user.get("Name") and user.get("Password") == p:
        print("Username or password isn't OK!")
    else:
        print("Welcome to app! You can go on...")
        break
# or
user = {'Marek': '1234'}
while True:
    n = input("Enter your username: ")
    p = input("Enter your password: ")
    if user.get(n) == p:
        print("Welcome to app! You can go on...")
        break
    else:
        print("Username or password isn't OK!")
