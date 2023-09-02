print(
'Twinkle, twinkle, little star,\n'
'\tHow I wonder what you are!\n'
'\t\tUp above the world so high,\n'
'\t\tLike a diamond in the sky.\n'
'Twinkle, twinkle, little star,\n'
'\tHow I wonder what you are'
)
#HEREDOC
print("""
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example
    """)
#CHARACTER
x = 64
print('%c' % (x))                                                   # @
#.FORMAT()
name, age = "Simon", 19                                             # Name: Simon
address = "Bangalore, Karnataka, India"                             ##Age: 19
print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))  ##Address: Bangalore, Karnataka, India
#or
print("Name: %s\nAge: %d\nAddress: %s" % (name, age, address))      # -//-
#or
print(f"Name: {name}\nAge: {age}\nAddress: {address}")              # -//-

x, y = 4, 3

print("({} + {}) ^ 2 = {}".format(x, y, x * x + 2 * x * y + y * y)) # (4 + 3) ^ 2) = 49
#or
final = x * x + 2 * x * y + y * y
print("({} + {}) ^ 2 = {}".format(x, y, final))                     # (4 + 3) ^ 2) = 49
#or
print("(%d + %d) ^ 2 = %d" % (x, y, final))                         # (4 + 3) ^ 2) = 49
#or
print("(%i + %i) ^ 2 = %i" % (x, y, final))                         # (4 + 3) ^ 2) = 49
#or
print(f"({x} + {y}) ^ 2 = {final}")                                 # (4 + 3) ^ 2) = 49
#CYCLE IN A LINE
for i in range(0, 10):
    print('*', end="")                                              # **********
#CYCLE IN A ROW
for i in range(1, 11):                                              #  1: 000000000010
    x = pow(10, i)                                                  ## 2: 000000000100 ...
    print(f'{i:>2}: {x:>012}')                                      ##10: 010000000000
#or
x = range(1, 11)                                                    #  1: 000000000010
for i in x:                                                         ## 2: 000000000100 ...
    print(f'{i:2d}: {x[-1] ** i:012d}')                             ##10: 010000000000