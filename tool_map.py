# MAP(), INPUT()
print("Enter a float to split: ", end='')               # 3.14
x, y = map(int, input().split("."))
print("First value after split:", x)                    # 3
print("Second value after split:", y)                   # 14
# MAP(), SUM()
lst = range(1, 10)                                      # [1, 2, 3, 4, 5, 6, 7, 8, 9]
move = range(99, 90, -1)                                # [99, 98, 97, 96, 95, 94, 93, 92, 91]
final = list(map(sum, zip(lst, move)))
print(final)                                            # [100, 100, 100, 100, 100, 100, 100, 100, 100]
