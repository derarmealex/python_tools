n = float(input('Input a number: '))
print('Number is Positive' if n > 0 else 'It is Zero!' if n == 0 else 'Number is Negative')

for stg in "abcd":                                                               # a3
    print(stg + "3")                                                             ##b3 ...
#or
for stg in "abcd": print(stg + "3")                                              # -//-
#print(stg + "3" for stg in "abcd")                                              # <generator object>
#print([stg + "3" for stg in "abcd"])                                            # ['a3', 'b3', 'c3', 'd3'

for stg2 in "go on", "waw":                                                      # go on
    print(stg2)                                                                  ##waw ...
#or
for stg2 in "go on", "waw": print(stg2)                                          # -//-
#print(stg2 for stg2 in ("go on", "waw"))                                        # <generator object>
#print([stg2 for stg2 in ("go on", "waw")])                                      # ['go on', 'waw']
    
for lst in [1, 2, 3, 4, 5]:                                                      # 1
    print(lst ** 2)                                                              ##4 ...
#or
for lst in [1, 2, 3, 4, 5]: print(lst ** 2)                                      # -//-
#print(lst ** 2 for lst in [1, 2, 3, 4, 5])                                      # <generator object>
#print([lst ** 2 for lst in [1, 2, 3, 4, 5]])                                    # [1, 4, 9, 16, 25]

for lst2 in ["a", "b", "c", "d"]:                                                # aa
    print(lst2 * 2)                                                              ##bb ...
#or
for lst2 in ["a", "b", "c", "d"]: print(lst2 * 2)                                # -//-
#print(lst2 * 2 for lst2 in ["a", "b", "c", "d"])                                # <generator object>
#print([lst2 * 2 for lst2 in ["a", "b", "c", "d"]])                              # ['aa', 'bb', 'cc', 'dd']

for dct in {"Name": "Alex", "Surname": "Green", "Password": "123"}:              # Name
    print(dct)                                                                   ##Surname ...
#or
for dct in {"Name": "Alex", "Surname": "Green", "Password": "123"}: print(dct)   # -//-
#print(dct for dct in {"Name": "Alex", "Surname": "Green", "Password": "123"})   # <generator object>
#print([dct for dct in {"Name": "Alex", "Surname": "Green", "Password": "123"}]) # ['Name', 'Surname', 'Password']

# ITERATION
lst3 = iter(["a", "b", "c"])
print(next(lst3) * 2)                                                            # aa
print(next(lst3))                                                                # b
print(next(lst3) + "e")                                                          # ce
print(next(lst3))                                                                # StopIteration
# or
lst3 = ["a", "b", "c"]
out = (x for x in lst3)
print(next(out) * 2)                                                             # aa
print(next(out))                                                                 # b
print(next(out) + "e")                                                           # ce
print(next(out))                                                                 # StopIteration
# or
lst3 = ["a", "b", "c"]
for x in lst3: print(x*2)                                                        # aa
                                                                                 ##bb ...
for x in lst3: print(x)                                                          # a
                                                                                 ##b ...
for x in lst3: print(x+'e')                                                      # ae
                                                                                 ##be ...
# GENERATION
def fung(x):
    for x in x:
        yield x * 2
        yield x
        yield x + 'e'
        yield x
f = fung(["a", "b", "c"])
print(next(f))                                                                   # aa
print(next(f))                                                                   # a
print(next(f))                                                                   # ae
print(next(f))                                                                   # a
print(next(f))                                                                   # 
print(next(f))                                                                   # bb
print(next(f))                                                                   # b
print(next(f))                                                                   # be ... StopIteration
