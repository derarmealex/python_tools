import random

final = []
for x in range(0, 10):
    final.append(random.randint(1, 10))                                         # [6, 8, 7, 10, 9, 8, 10, 2, 8, 3]
print(final)
# or
print(', '.join(['' + str(random.randint(1, 10)) for x in str(range(0, 10))]))  # 6, 8, 7, 10, 9, 8, 10, 2, 8, 3
# or
print(', '.join([str(random.choice(range(1, 10))) for x in range(0, 10)]))      # 6, 8, 7, 10, 9, 8, 10, 2, 8, 3
# or
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#print(random.shuffle(x))                                                        # None
random.shuffle(x)
print(x)                                                                        # [6, 8, 7, 10, 9, 8, 10, 2, 8, 3]
