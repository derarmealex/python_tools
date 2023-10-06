# TO STRING
gifts = ("Camera", "Headphones", "Watches")

gifts2 = ", ".join(gifts)
print(gifts2)                                           # Camera, Headphones, Watches
# or
print(", ".join(gifts))                                 # Camera, Headphones, Watches
# TO LIST OF STRINGS
sample = ['Java', 'Python', '1', 1]

a = []
for i in sample:
    a.append(str(i))
print(a)                                                # ['Java', 'Python', '1', '1']
# or
print([str(i) for i in sample])                         # ['Java', 'Python', '1', '1']
# TO STRING
print(", ".join(a))                                     # Java, Python, 1, 1
# or
print(", ".join([str(i) for i in sample]))              # Java, Python, 1, 1
# or
sample = ["11", "33", "50"]

sample2 = sample[0] + ', ' + sample[1] + ', ' + sample[2]
print(sample2)                                          # 11, 33, 50
# or
print(', '.join(sample))                                # 11, 33, 50
# TO LIST OF INTEGERS
sample = [int(i) for i in sample]                       # [11, 33, 50]
print(sum(sample))                                      # 94
# EXTRACT JUST NUMBERS
sample = ["11", "33.5", "50"]

sample = [float(i) for i in sample]                     # [11.0, 33.5, 50.0]
print(sum(sample))                                      # 94.5
# MIX
sample = ['wood', '11', 33, 50]
sample = ['' + str(x) for x in sample]                  # ['wood', '11', '33', '50']

sample2 = []                                            # [11, 33, 50]

for x in sample:
    if not x.isnumeric():
        continue
    sample2.append(int(x))
print(sum(sample2))                                     # 94
# or
for x in sample:
    if x.isnumeric():
        sample2.append(int(x))
print(sum(sample2))                                     # 94
# or
sample2 = [int(x) for x in sample if x.isdigit()]       # [11, 33, 50]
print(sum(sample2))                                     # 94
# or
print(sum([int(x) for x in sample if x.isdigit()]))     # 94
