def func(x, n):
    return x * n

print(func(2, 6))                               # 12
print(func(3, 6))                               # 18
# or
x = 2
n = 6
print(func(x, n))                               # 12

a = lambda x, n: x * n
print(a(2, 6))                                  # 12
print(a(3, 6))                                  # 18
# or
def func(n):
    return lambda x : x * n
myd = func(2)
myt = func(3)
print(myd(6))                                   # 12
print(myt(6))                                   # 18
# or
print(func(2)(6))                               # 12
print(func(3)(6))                               # 18
