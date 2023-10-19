# bool()
# all()             True if every element is True
# any()             True if at least 1 element is True
# isinstance()

# ISINSTANCE()
a = 10
b = 20.23
c = "10"


def add_numbers(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    return "Inputs must be integers!"


print(add_numbers(a, a))                                # 20
print(add_numbers(a, b))                                # Inputs must be integers!


# or
print(a == int(a))                                      # True
print(a == str(a))                                      # False
print(a == float(a))                                    # True

print(b == int(b))                                      # False
print(b == str(b))                                      # False
print(b == float(b))                                    # True

print(c == int(c))                                      # False
print(c == str(c))                                      # True
print(c == float(c))                                    # False
# ANY()
print("any()")
x = [3, 399, -3, 99]
print(any(x))                                           # True
print(any(isinstance(x, str) for x in x))               # False
print(any(9 for x in x))                                # True
print(any('-' for x in x))                              # True
print(any(0 for x in x))                                # False

num = [2, 3, 4, 5]
print(all(x > 1 for x in num))                          # True
print(all(x > 4 for x in num))                          # False
# TRUE/FALSE TO 1/0
x = True
y = False
print(int(x))                                           # 1
print(int(y))                                           # 0
# 1/0 TO TRUE/FALSE
x = 1
y = 0
print(bool(x))                                          # True
print(bool(y))                                          # False
# BOOL() 1 or 0
while True:
    ctr_ques = input("Are you in IDLE now? \n1 - 'yes' 0 - 'no': ").strip()
# 0, 1, 2
    if int(ctr_ques) in range(0, 2):
        ctr_ques = bool(int(ctr_ques))
        if ctr_ques:
            print("\n\tThat's true\n")                  # 1 - That's true
        else:
            print("\n\tThat's a lie!..\n")              # 0 - That's a lie!..
    else:
        print("\n\tEnter 1 or 0!\n")                    # 2 - Enter 1 or 0!
# GENERALLY
while True:
    x = input("Enter a number: ").strip()               # 0, 1, 99
    if x.isnumeric():
        x = int(x)
        if bool(x):
            print("\n\tThat's True\n")                  # 1 - That's True, 99 - That's True
        else:
            print("\n\tThat's False\n")                 # 0 - That's False
    else:
        print("\n\tEnter a number!\n")


# IF THERE'S ALLWAYS 1 AFTER 0
def test(stg):
    while '01' in stg:
        stg = stg.replace('01', '')
    return len(stg) == 0


stg = "01010101"
print("If there's allways 1 after 0 in the sequence:", stg)
print(test(stg))                                        # True
stg = "00"
print("If there's allways 1 after 0 in the sequence:", stg)
print(test(stg))                                        # False
stg = "000111000111"
print("If there's allways 1 after 0 in the sequence:", stg)
print(test(stg))                                        # True
stg = "00011100011"
print("If there's allways 1 after 0 in the sequence:", stg)
print(test(stg))                                        # False


# EXAMPLE
while True:
    x = int(input('Enter a number: '))                  # 34, 5
    if x <= 17:
        print(17 - x)                                   # 12
    else:
        print(abs(17 - x) * 2)                          # 34


# or
def dif(z):
    if z <= 17:
        return 17 - z
    return abs(17 - z) * 2


print(dif(34))                                          # 34
print(dif(5))                                           # 12


# EXAMPLE
def ctr(x):
    if 1100 >= x >= 900 or 2100 >= x >= 1900:
        return True
    return False


print(ctr(899))                                         # False
print(ctr(900))                                         # True
print(ctr(1100))                                        # True
print(ctr(1101))                                        # False

print(ctr(1899))                                        # False
print(ctr(1900))                                        # True
print(ctr(2100))                                        # True
print(ctr(2101))                                        # False


# or
def ctr(z, y=1000):
    return abs(y - z) <= 100 or abs(y - z) <= 100


print(ctr(899))                                         # False
print(ctr(900))                                         # True
print(ctr(1100))                                        # True
print(ctr(1101))                                        # False

print(ctr(1899, 2000))                                  # False
print(ctr(1900, 2000))                                  # True
print(ctr(2100, 2000))                                  # True
print(ctr(2101, 2000))                                  # False


# EXAMPLE
def calc(x, y, z):
    if x == y == z:
        return (x + y + z) * 3
    return x + y + z


# or
def calc(x, y, z):
    summus = x + y + z
    if x == y == z:
        summus *= 3
    return summus


print(calc(3, 3, 3))
print(calc(3, 99, 3))
print(calc(3, 399, -3))


# ALL()
def test(num, n):
    return all(x > n for x in num)


num = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(test(num, 12))                                    # False
print(test(num, 5))                                     # True
