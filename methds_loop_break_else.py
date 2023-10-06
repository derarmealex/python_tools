for letter in ("a", "b", "c", "d"):                             # A
    print(letter.upper())                                       ##B
else:                                                           ##C
    print("All the letters are written down")                   ##D
                                                                ##All the letters are written down
for letter in ("a", "b", "c", "d"):
    if letter == "4":
        print("Found '4', skip the cycle")
        break
else:
    print("All the letters are written down")                   # All the letters are written down
print("Go on the loop")                                         ##Go on the loop

for letter in ("a", "b", "c", "d"):
    if letter == "c":
        print("Found 'c', skip the cycle")
        break
else:
    print("All the letters are written down")                   # Found 'c', skip the cycle
print("Go on the loop")                                         ##Go on the loop
