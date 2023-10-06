stg = "1, 2, 3, 4, 5"

stg2 = stg.split(",")                                   # ['1', ' 2', ' 3', ' 4', ' 5']

final = []
for item in stg2:
    clear = int(item.strip())
    final.append(clear)
print(final)                                            # [1, 2, 3, 4, 5]
# or
final = [int(item.strip()) for item in stg2]
print(final)                                            # [1, 2, 3, 4, 5]
# or
print([int(item.strip()) for item in stg2])             # [1, 2, 3, 4, 5]
