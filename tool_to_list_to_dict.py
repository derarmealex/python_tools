sequence = [1, 3, 5, 1, 2, 2, 32, 9, 1, 3, 1]
counts = dict()
for number in sequence:
    if number not in counts:
        counts[number] = 1                              # Key: 1 Value: 4
    else:                                               ##Key: 2 Value: 2
#        counts[number] = counts[number] + 1            ##Key: 3 Value: 2
        counts[number] +=1                              ##Key: 5 Value: 1
for key, value in sorted(counts.items()):               ##Key: 9 Value: 1
    print("Key:", key, "Value:", value)                 ##Key: 32 Value: 1
