# +=
# -=
# *=
# /=
# %=
# //=
# **=
# &=
# |=
# ^=
# >>=
# <<=

x = 1
while x <= 5:
    print(x)
#    x = x + 1
    x += 1
# or
x = [1]
for y in x:
    if y < 6:
        print(y)
        x.append(y + 1)

import time
x = 99999999999
while x > 0:
#    x = x // 3
    x //= 3
    time.sleep(0.5)
    print(x)
