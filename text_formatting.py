# format() - 2 arguments
# .format() - many arguments
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
# .FORMAT()
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

exam_st_date = (11, 12, 2024)
print('The examination will start from: %i/%i/%i' % exam_st_date)   # The examination will start from: 11/12/2024

color_list = ["Red", "Green", "White", "Black"]
print(color_list[-1], 'and', color_list[2])                         # Black and White
# or
color_list = ["Red", "Green", "White", "Black"]
print("%s and %s" % (color_list[-1], color_list[2]))                # Black and White

x = (input('Enter an integer number: '))                            # 5
print(int(x) + int(x + x) + int(x + x + x))                         # 615
print(int('%s' % x) + int('%s%s' % (x, x)) + int('%s%s%s' % (x, x, x)))  # 615
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
# ALIGNMENT
stg = '122.22'
stg2 = float(stg)

print(f'{stg2:.010f}')                                              # 122.2200000000
print(f'{stg2:.010}')                                               # 122.22
print(f'{stg2:010f}')                                               # 122.220000
print(f'{stg2:010}')                                                # 0000122.22
print(f'{stg2:01f}')                                                # 122.220000
print(f'{stg2:01}')                                                 # 122.22
print(f'{stg2:.10f}')                                               # 122.2200000000
print(f'{stg2:.10}')                                                # 122.22
print(f'{stg2:10f}')                                                # 122.220000
print(f'{stg2:10}')                                                 #     122.22
print(f'{stg2:.1f}')                                                # 122.2
print(f'{stg2:.1}')                                                 # 1e+02
print(f'{stg2:1f}')                                                 # 122.220000
print(f'{stg2:1}')                                                  # 122.22
print(f'{stg2:.0f}')                                                # 122
print(f'{stg2:.0}')                                                 # 1e+02
print(f'{stg2:0f}')                                                 # 122.220000
print(f'{stg2:0}')                                                  # 122.22
#print(f'{stg2:.f}')                                                 # ValueError
#print(f'{stg2:.}')                                                  # ValueError
print(f'{stg2:f}')                                                  # 122.220000
print(f'{stg2}')                                                    # 122.22

print(f'{stg2:.010f}')                                              # 122.2200000000
print(f'{stg2:.010}')                                               # 122.22
print(f'{stg2:2.010f}')                                             # 122.2200000000
print(f'{stg2:2.010}')                                              # 122.22
print(f'{stg2:2.10f}')                                              # 122.2200000000
print(f'{stg2:2.10}')                                               # 122.22
print(f'{stg2:010.2f}')                                             # 0000122.22
print(f'{stg2:010.2}')                                              # 0001.2e+02
print(f'{stg2:10.2f}')                                              #     122.22
print(f'{stg2:10.2}')                                               #    1.2e+02
# ALIGNMENT WITH ZEROES - LEFT SIDE
print(f'{stg2:>010}')                                               # 0000122.22
print(f'{stg2:010}')                                                # 0000122.22
# or
print('{:>010}'.format(stg2))                                       # 0000122.22
print('{:010}'.format(stg2))                                        # 0000122.22
print(format(stg2, '010'))                                          # 0000122.22
# or
print('%010.2f' % stg2)                                             # 0000122.22
# or
print(stg.rjust(10, '0'))                                           # 0000122.22
# ALIGNMENT WITH ZEROES - RIGHT SIDE
print(f'{stg2:<010}')                                               # 122.220000
# or
print('{:<010}'.format(stg2))                                       # 122.220000
print(format(stg2, '010f'))                                         # 122.220000
# or
print('%f' % stg2)                                                  # 122.220000
# or
print(stg.ljust(10, '0'))                                           # 122.220000
# NUMERALS WITH COMMAS
z = 1000000
print(f'{z:,d}')                                                    # 1,000,000
print(f'{z:,.2f}')                                                  # 1,000,000.00
