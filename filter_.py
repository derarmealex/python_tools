# FILTER BY A CONDITION
def filter_odd_num(in_num):
    if(in_num % 2) == 0:
        return True
    else:
        return False


numbers = [1, 2, 4, 5, 7, 8, 10, 11]
out_filter = filter(filter_odd_num, numbers)
print("Filtered list:", list(out_filter))                               # Filtered list: [2, 4, 8, 10]
# FILTER BY A LIST
list_of_stop_words = ["me", "on", "s", "'"]
string_to_process = "Somebody tells me what's going on here?"
split_str = string_to_process.split()
filtered_str = ' '.join(filter(lambda s: s not in list_of_stop_words, split_str))
print(filtered_str)                                                     # Somebody tells what's going here?


# FILTER OF DUPLICATES
def filter_duplicate(string_to_check):
    if string_to_check in ctr:
        return False
    else:
        return True


lst = ["Python", "CSharp", "Java", "Go"]
lst2 = ["Python", "Scala", "JavaScript", "Go", "PHP", "CSharp"]


ctr = lst2
out_filter = list(filter(filter_duplicate, lst))
ctr = lst
out_filter += list(filter(filter_duplicate, lst2))
print(out_filter)                                                       # [‘Java’, ‘Scala’, ‘JavaScript’, ‘PHP’]
#or
x = [x for x in lst2 if x not in lst]
y = [x for x in lst if x not in lst2]
print(y + x)                                                            # ['Java', 'Scala', 'JavaScript', 'PHP']


# INTERSECTION
def interSection(arr1, arr2):
    out = list(filter(lambda it: it not in arr1, arr2))                # dev2
    print(''.join(out))
    out = list(filter(lambda it: it not in arr2, arr1))                # thon3
    print(''.join(out))
    out = list(filter(lambda it: it in arr1, arr2))                    # Py .0
    print(''.join(out))
    out = list(filter(lambda it: it in arr2, arr1))
    print(''.join(out))                                                # Py .0
    return out


arr1 = 'Python 3.0'
arr2 = 'Pydev 2.0'


if __name__ == "__main__":
    print(interSection(arr1, arr2))                                    # [‘p’, ‘y’, ‘ ‘, ‘.’, ‘0’]
# BOOL FILTER
bools = ['bool', 0, None, True, False, 1, 1 - 1, 2 % 2]                # 1 0 0 1 0 1 0 0
out = filter(None, bools)
print([i for i in out])                                                # ['bool', True, 1]
