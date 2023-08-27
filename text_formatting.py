print(
'Twinkle, twinkle, little star,\n'
'\tHow I wonder what you are!\n'
'\t\tUp above the world so high,\n'
'\t\tLike a diamond in the sky.\n'
'Twinkle, twinkle, little star,\n'
'\tHow I wonder what you are'
)
# HEREDOC
print("""
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example
    """)
# .FORMAT()
name, age = "Simon", 19                                             # Name: Simon
address = "Bangalore, Karnataka, India"                             ##Age: 19
print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))  ##Address: Bangalore, Karnataka, India

x, y = 4, 3
result = x * x + 2 * x * y + y * y
print("({} + {}) ^ 2) = {}".format(x, y, result))
