# \n - nový řádek
# \t - tabulátor
# \a - zvonek (sekvecne pro pípnutí)
# \\ - zpětné lomítko se píše jako \\ , protože jedním \ začínají speciální znaky
# \' - jednoduché uvozovky
# \" - dvojité uvozovky

print(
'Twinkle, twinkle, little star,\n'
'\tHow I wonder what you are!\n'
'\t\tUp above the world so high,\n'
'\t\tLike a diamond in the sky.\n'
'Twinkle, twinkle, little star,\n'
'\tHow I wonder what you are'
    )
# HEREDOC
print(
    """
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example
    """
    )
# CHARACTER
x = 64
print('%c' % x)                                                     # @
# FORMAT
name, age = "Simon", 19                                             # Name: Simon
address = "Bangalore, Karnataka, India"                             ##Age: 19
print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))  ##Address: Bangalore, Karnataka, India
# or
print("Name: %s\nAge: %d\nAddress: %s" % (name, age, address))      # -//-
# or
print(f"Name: {name}\nAge: {age}\nAddress: {address}")              # -//-

x, y = 4, 3

print("({} + {}) ^ 2 = {}".format(x, y, x * x + 2 * x * y + y * y)) # (4 + 3) ^ 2) = 49
# or
final = x * x + 2 * x * y + y * y
print("({} + {}) ^ 2 = {}".format(x, y, final))                     # (4 + 3) ^ 2) = 49
# or
print("(%d + %d) ^ 2 = %d" % (x, y, final))                         # (4 + 3) ^ 2) = 49
# or
print("(%i + %i) ^ 2 = %i" % (x, y, final))                         # (4 + 3) ^ 2) = 49
# or
print(f"({x} + {y}) ^ 2 = {final}")                                 # (4 + 3) ^ 2) = 49
# CYCLE IN A LINE
for i in range(0, 10):
    print('*', end="")                                              # **********
# CYCLE IN A ROW WITH LEADING ZEROES
for i in range(1, 11):                                              #  1: 000000000010
    x = pow(10, i)                                                  ## 2: 000000000100 ...
    print(f'{i:>2}: {x:>012}')                                      ##10: 010000000000
# or
x = range(1, 11)                                                    #  1: 000000000010
for i in x:                                                         ## 2: 000000000100 ...
    print(f'{i:2}: {x[-1] ** i:012}')                               ##10: 010000000000
# ALIGNMENT WITH ZEROES - LEFT SIDE
stg = '122.22'
stg2 = float(stg)

print(f'{stg2:>010}')                                               # 0000122.22
print(f'{stg2:010}')                                                # 0000122.22
# or
print('{:>010}'.format(stg2))                                       # 0000122.22
print('{:010}'.format(stg2))                                        # 0000122.22
# or
print('%010.2f' % stg2)                                             # 0000122.22
# or
print(stg.rjust(10, '0'))                                           # 0000122.22
# ALIGNMENT WITH ZEROES - RIGHT SIDE
print(f'{stg2:<010f}')                                              # 122.220000
print(f'{stg2:010f}')                                               # 122.220000
# or
print('{:<010f}'.format(stg2))                                      # 122.220000
print('{:010f}'.format(stg2))                                       # 122.220000
# or
print('%f' % stg2)                                                  # 122.220000
# or
print(stg.ljust(10, '0'))                                           # 122.220000
# NUMERALS WITH COMMAS
z = 1000000
print(f'{z:,d}')                                                    # 1,000,000
print(f'{z:,.2f}')                                                  # 1,000,000.00
