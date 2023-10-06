a, i, j, k = "Hey", "Hello", 55, 21.0765
print(k, j, i, a)                           # 21.0765 55 Hello Hey
print(j + k)                                # 76.0765
print(a + i, sep=" ")                       # HeyHello
print(a, i, sep=", ")                       # Hey, Hello
print(a, i)                                 # Hey Hello
# SWAP
x = 1
y = 99
temp = x
x = y
y = temp
print(x, y)                                 # 99 1
# or
x, y = y, x
print(x, y)                                 # 99, 1
# RETURN EMPTIES
print(type(x)(), type(y)(), sep=', ')       # 0, 0
