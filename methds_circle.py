# QUAD-CIRCLE
for x in range(1, 11):                                          # 10 20 30 40 50 60 70 80 90 100
    for x in range(1, 11):                                      # 10 20 30 40 50 60 70 80 90 100
        print(x * 10, end=' ')                                  # 10 20 30 40 50 60 70 80 90 100
    print('')                                                   # 10 20 30 40 50 60 70 80 90 100 ... 10x
# or
for x in range(1, 11):
    for y in range(1, 11):
        if x + y % 2:
            print(x * 10, end=' ')
        else:                                                   # 10 10 10 10 10 10 10 10 10 10
            print(x * 50, end=' ')                              # 20 20 20 20 20 20 20 20 20 20
    print('')                                                   # 90 90 90 90 90 90 90 90 90 90 ... 10x
# CIRCLE-IN-CIRCLE
lst = [
    "Matous", "Marek", "Lukas", "Jan",
    "Lucie", "Aneta", "Eva", "Lenka",
    "Helmut", "Hammet", "Hetfield", "Harold"
    ]
for name in lst:                                                # M
    for letter in name:                                         ##a
        print(letter)                                           ##t...
# or
a = [lst for lst in lst for lst in lst]                         # M
for a in a:                                                     ##a
    print(a)                                                    ##t ...
# or
print([lst for lst in lst for lst in lst])                      # ['M', 'a', 't', ...
# INTERSECTION-CIRCLE
adj = ['dark', 'light', 'brown', 'green']                       # dark wood
noun = ['wood', 'mount', 'river', 'sky']                        ##dark mount ...
for x in adj:                                                   ##... light river
    for y in noun:                                              ##light sky ...
        print(x, y)                                             ##... green sky
# IMMERSED CIRCLE
lpdlst = [
  ["Matous", "Marek", "Lukas", "Jan"],
  ["Lucie", "Aneta", "Eva", "Lenka"],
  ["Helmut", "Hammet", "Hetfield", "Harold"]
]
for lst in lpdlst:                                              # M
    for name in lst:                                            ##a
        for letter in name:                                     ##t
            print(letter)                                       ##...
# or
a = [lst for lst in lpdlst for lst in lst for lst in lst]       # ['M', 'a', 't', 'o', 'u', ...
for a in a:                                                     # M
    print(a)                                                    ##a ...

print([lst for lst in lpdlst for lst in lst])                   #['Matous', 'Marek', 'Lukas', 'Jan', ...
