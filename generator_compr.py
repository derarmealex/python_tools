n = float(input('Input a number: '))
print('Number is Positive' if n > 0 else 'It is Zero!' if n == 0 else 'Number is Negative')

for stg in "abcd":                                                               # a3
    print(stg + "3")                                                             ##b3 ...
# or
for stg in "abcd": print(stg + "3")                                              # -//-
for stg in "abcd": print(stg + "3", end=' ')                                     # a3 b3 c3 d3
print(stg + "3" for stg in "abcd")                                               # <generator object>
# or
print([stg + "3" for stg in "abcd"])                                             # ['a3', 'b3', 'c3', 'd3']

for stg in "go on", "waw":                                                       # go on
    print(stg)                                                                   ##waw ...
# or
for stg in "go on", "waw": print(stg)                                            # -//-
print(stg2 for stg2 in ("go on", "waw"))                                         # <generator object>
# or
print([stg2 for stg2 in ("go on", "waw")])                                       # ['go on', 'waw']

for lst in [1, 2, 3, 4, 5]:                                                      # 1
    print(lst ** 2)                                                              ##4 ...
# or
for lst in [1, 2, 3, 4, 5]: print(lst ** 2)                                      # -//-
print(lst ** 2 for lst in [1, 2, 3, 4, 5])                                       # <generator object>
# or
print([lst ** 2 for lst in [1, 2, 3, 4, 5]])                                     # [1, 4, 9, 16, 25]

for lst in ["a", "b", "c", "d"]:                                                 # aa
    print(lst * 2)                                                               ##bb ...
# or
for lst in ["a", "b", "c", "d"]: print(lst * 2)                                  # -//-
print(lst * 2 for lst in ["a", "b", "c", "d"])                                   # <generator object>
# or
print([lst * 2 for lst in ["a", "b", "c", "d"]])                                 # ['aa', 'bb', 'cc', 'dd']

for dct in {"Name": "Alex", "Surname": "Green", "Password": "123"}:              # Name
    print(dct)                                                                   ##Surname ...
# or
for dct in {"Name": "Alex", "Surname": "Green", "Password": "123"}: print(dct)   # -//-
print(dct for dct in {"Name": "Alex", "Surname": "Green", "Password": "123"})    # <generator object>
# or
print([dct for dct in {"Name": "Alex", "Surname": "Green", "Password": "123"}])  # ['Name', 'Surname', 'Password']

# ITERATION
lst = ["a", "b", "c"]

lst2 = iter(lst)
print(next(lst2) * 2)                                                            # aa
print(next(lst2))                                                                # b
print(next(lst2) + "e")                                                          # ce
print(next(lst2))                                                                # StopIteration
# or
out = (x for x in lst)                                                           # Generator
print(next(out) * 2)                                                             # aa
print(next(out))                                                                 # b
print(next(out) + "e")                                                           # ce
print(next(out))                                                                 # StopIteration
# or
for x in lst: print(x * 2)                                                       # aa
                                                                                 ##bb ...
for x in lst: print(x)                                                           # a
                                                                                 ##b ...
for x in lst: print(x + 'e')                                                     # ae
                                                                                 ##be ...


# GENERATION
def fungus(x):
    for x in x:
        yield x * 2
        yield x
        yield x + 'e'


f = fungus(["a", "b"])
print(next(f))                                                                   # aa
print(next(f))                                                                   # a
print(next(f))                                                                   # ae
print(next(f))                                                                   # a
print(next(f))                                                                   # bb
print(next(f))                                                                   # b
print(next(f))                                                                   # be
print(next(f))                                                                   # StopIteration
