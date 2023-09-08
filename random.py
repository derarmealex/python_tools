import random
final = []
for x in range(0, 10):
    final.append(random.randint(1, 10))                                           # [5, 6, 2, 3, 3, 10, 10, 9, 1, 7, 8, 7]
print(final)
#or
final = (', '.join(['' + str(random.randint(1, 10)) for x in str(range(0, 10))]))
print(final)                                                                      # 5, 6, 2, 3, 3, 10, 10, 9, 1, 7, 8, 7