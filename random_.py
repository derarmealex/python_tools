import random

final = []
for x in range(0, 10):
    final.append(random.randint(1, 10))                                          # [5, 6, 2, 3, 3, 10, 10, 9, 1, 7, 8, 7]
print(final)
#or
print(', '.join(['' + str(random.randint(1, 10)) for x in str(range(0, 10))]))   # 5, 6, 2, 3, 3, 10, 10, 9, 1, 7, 8, 7
#or
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

random.shuffle(x)
print(x)                                                                         # 5, 6, 2, 3, 3, 10, 10, 9, 1, 7, 8, 7
#or
print(', '.join([str(random.choice(x)) for i in range(0, 10)]))                  # 5, 6, 2, 3, 3, 10, 10, 9, 1, 7, 8, 7