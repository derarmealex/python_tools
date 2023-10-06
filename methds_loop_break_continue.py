mlt_three = []
number = (1, 2, 3, 4, 5, 6, 7)
for number in number:
    if number % 3 == 0:
        mlt_three.append(number)
        break
print("found multiple of three:", mlt_three)    # found multiple of three: [3]

for sentence in "be near":                      # Value b is important
    if sentence in {"e", "r"}:                  ##Value   is important
        continue                                ##Value n is important
    print("Value", sentence, "is important")    ##Value a is important
print(sentence)                                 ##r
