# .copy()
# .count()
# .find()
# .index()
# .replace(old, new[, count])
# .upper(), isupper()
# .lower(), islower()
# .strip(), lstrip(), rstrip()
# .split()
# .join()
# sorted()
# reversed()
# len()
# sep=()
# end=()
# [::]
# str.isidentifier()  Определение, есть ли строка идентификатором или ключевым словом
# str.isalpha()       if there's only letters and there's at least one
# str.isdigit()       if there's only numbers and there's at least one
# str.isalnum()       if there's only letters or numbers and there's at least one
# str.isascii()       Проверка ASCII-символов строки
# str.isdecimal()     Проверка десятичных символов строки
# str.isnumeric()     Проверка числовых символов в строке
# str.isprintable()   Проверка печатаемых символов строки
# str.isspace()       Определение пробельных символов строки
# str.istitle()       Определение заглавия строки
# str.islower()       if there's only lowercase symbols
# str.isupper()       if there's only uppercase symbols

# OUTPUT
print("Hello", "World")                             # Hello World
print("Hello" "World")                              # HelloWorld
print("Hello, my World")                            # Hello, my World
print("Hello," "my" "World")                        # Hello,myWorld
print("Hello," "my" "World", sep=" ", end='\n')     # Hello,myWorld
print("Hello,", "my", "World", sep="")              # Hello,myWorld
print("Hello,", "my", "World")                      # Hello, my World

# SORT
stg = "Hello", "World"                              # tuple
stg2 = "Hello, World"                               # string

print(sorted(stg2))                                 # [' ', ',', 'H', 'W', 'd', 'e', 'l', 'l', 'l', 'o', 'o', 'r']
print(''.join(sorted(stg2)))                        #  ,HWdellloor
# SPLIT

#y = x.split(" ")[0]
#z = x.split(" ")[1]
x, y = stg2.split(" ")
print(x[0])                                         # H
print(y[0])                                         # W
# MAP
print(",".join(stg2))                               # H,e,l,l,o,W,o,r,l,d
print(stg2.count('l'))                              # 3
print(stg2.count('l', 1, 2))                        # 0 ==  # print(stg2[1:2].count('l'))
print(stg2.find('h'))                               # -1
print(stg2.find('o'))                               # 4
#print(stg2.index('h'))                              # ValueError
print(stg2.index('o'))                              # 4
print(len(stg2))                                    # 12
print(stg2.lower())                                 # hello, world
print(stg2.upper())                                 # HELLO, WORLD
print(stg2.split("l"))                              # ['He', '', 'o, Wor', 'd']
print(stg2.split())                                 # ['Hello,', 'World']

print(stg)                                          # ('Hello', 'World')
print(stg2)                                         # Hello, World
print(stg2[-7:-1])                                  # , Worl
print(stg2[::2])                                    # Hlo ol
print(stg2[:4])                                     # Hell
print("%.4s" % stg2)                                # Hell
print("{:.4s}".format(stg2))                        # Hell
print(f"{stg2:.4s}")                                # Hell
# REPLACE
#print(x[0] = 1)                                     # TypeError
print(stg2.replace('World', 'Hell'))                # Hello, Hell
# or
import re
print(re.sub('l', 'd', stg2))                       # Heddo, Hedd
print(re.sub('d', 'l', stg2, 2))                    # Hello, Hedd
# REVERSE
x = 'forest'

#x.reverse()                                         # AttributeError
for i in reversed(x):
    print(i, end='')                                # tserof
# or
print(''.join(reversed(x)))                         # tserof
# or
print(x[::-1])                                      # tserof
# CONCATENATE
stg = 'Oh'
stg2 = 'my'
stg3 = 'God'

x = stg, stg2, stg3
print(' '.join(x))                                              # Oh my God
# or
print(stg + ', ' + stg2 + ' ' + stg3)                           # Oh, my God
# or
print('%s, %s %s' % x)                                          # Oh, my God
# or
final = stg + ', ' + stg2 + ' ' + stg3
print('{} + , + {} + {} = {}'.format(stg, stg2, stg3, final))   # Oh + , + my + God = Oh, my God
# or
print('{} + , + {} + {} = {}'.format(stg, stg2, stg3, stg + ', ' + stg2 + ' ' + stg3))
                                                                # Oh + , + my + God = Oh, my God
# or
print(f'{stg} + , + {stg2} + {stg3} = {final}')                 # Oh + , + my + God = Oh, my God
# BOOL
x = "Oh, my God"

#print(x[0] = 1)                                   # TypeError
print(x[0] == 1)                                    # False
print(x[0] == 'O')                                  # True

print(x.startswith("Oh my"))                        # False
print(x.startswith("Oh, my"))                       # True
print(x.startswith("oh, my"))                       # False
print(x.startswith("God"))                          # False

print(x.endswith("God"))                            # True
print(x.endswith("god"))                            # False
print(x.endswith("God "))                           # False
print(x.endswith("Oh, my"))                         # False

print("my" in x)                                    # True
print("my " in x)                                   # True
print(" my" in x)                                   # True
print("My" in x)                                    # False

print("od" in x)                                    # True
print("Od" in x)                                    # False

x = x.upper()                                       # 'OH, MY GOD'
print([x for x in x if x.islower()])                # []
print(any(x.islower() for x in x))                  # False
print(''.join([x for x in x if x.isupper()]))       # OHMYGOD
print(any(x.isupper() for x in x))                  # True

x = "9Oh, my God"
print(isinstance(x, int))                           # False
print(isinstance(x, str))                           # True
print(isinstance(x[0], int))                        # False
print(isinstance(int(x[0]), int))                   # True
