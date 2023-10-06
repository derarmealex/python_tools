def fungus(x, n):
    return x * n


print(fungus(2, 6))                             # 12
print(fungus(3, 6))                             # 18
# or
a = lambda x, n: x * n
print(a(2, 6))                                  # 12
print(a(3, 6))                                  # 18


# or
def fungus(n):
    return lambda x: x * n


myd = fungus(2)
myt = fungus(3)
print(myd(6))                                   # 12
print(myt(6))                                   # 18
# or
print(fungus(2)(6))                             # 12
print(fungus(3)(6))                             # 18
