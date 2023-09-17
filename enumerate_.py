names = ["John", "Jane", "Doe"]
# FORMAT: START WITH ANY NUMBER
enumNames = enumerate(names, 10)
print(list(enumNames))                                  # [(10, 'John'), (11, 'Jane'), (12, 'Doe')]
# FORMAT
enumNames = enumerate(names)
print(enumNames)                                        # <enumerate object at 0x0000022DAE05E520>
print(enumerate(names))                                 # <enumerate object>
print(list(enumNames))                                  # [(0, 'John'), (1, 'Jane'), (2, 'Doe')]
print(dict(enumerate(names)))                           # {0: 'John', 1: 'Jane', 2: 'Doe'}
# OUTPUT
print([n for n in names])                               # ['John', 'Jane', 'Doe']
print([n for n in enumNames])                           # [(0, 'John'), (1, 'Jane'), (2, 'Doe')]

enumNames = enumerate(names, 1)
for n, x in enumNames:
    print(f"№ {n} ==> {x}")                             # № 1 ==> John
                                                        ##№ 2 ==> Jane
                                                        ##№ 3 ==> Doe
# GENERATOR
print(next(enumNames))                                  # (1, 'John')
print(next(enumNames))                                  # (2, 'Jane')
print(next(enumNames))                                  # (3, 'Doe')
print(next(enumNames))                                  # StopIteration
# EXTRACTION AND PROCESSING INDEXES
lst = [10, 20, 30, 40]

ix = 0
for number in lst:
    lst[ix] += 5
    ix += 1
print(lst)                                              # [15, 25, 35, 45]
# or
for number in range(len(lst)):
    lst[number] += 5
print(lst)                                              # [15, 25, 35, 45]
# or
print([lst[number] + 5 for number in range(len(lst))])  # [15, 25, 35, 45]
# or
for ix, number in enumerate(lst):
    lst[ix] += 5
print(lst)                                              # [15, 25, 35, 45]
# or
print([number + 5 for ix, number in enumerate(lst)])    # [15, 25, 35, 45]
