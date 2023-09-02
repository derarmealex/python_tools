numbers = [1, 2, 4, 5, 7, 8, 10, 11]
def filter_odd_num(in_num):
    if(in_num % 2) == 0:
        return True
    else:
        return False
out_filter = filter(filter_odd_num, numbers)
print("Filtered list: ", list(out_filter))                                          # [2, 4, 8, 10]

list1 = ["Python", "CSharp", "Java", "Go"]
list2 = ["Python", "Scala", "JavaScript", "Go", "PHP", "CSharp"]
def filter_duplicate(string_to_check):
    if string_to_check in ll:
        return False
    else:
        return True
ll = list2
out_filter = list(filter(filter_duplicate, list2))
ll = list1
out_filter += list(filter(filter_duplicate, list1))
print(out_filter)                                                          # [‘Java’, ‘Scala’, ‘JavaScript’, ‘PHP’]

list_of_stop_words = ["в", "и", "по", "за"]
string_to_process = "Сервис по поиску работы и сотрудников HeadHunter "
"опубликовал подборку высокооплачиваемых вакансий в России за август."
split_str = string_to_process.split()
filtered_str = ' '.join((filter(lambda s: s not in list_of_stop_words, split_str)))
print(filtered_str)                                                        # Сервис поиску работы сотрудников HeadHunter

arr1 = ['p','y','t','h','o','n',' ','3','.','0']
arr2 = ['p','y','d','e','v',' ','2','.','0']
def interSection(arr1, arr2):
    out = list(filter(lambda it: it in arr1, arr2))
    return out
if __name__ == "__main__":
    out = interSection(arr1, arr2)
    print(out)                                                             # [‘p’, ‘y’, ‘ ‘, ‘.’, ‘0’]

bools = ['bool', 0, None, True, False, 1, 1-1, 2%2]
out = filter(None, bools)
print([iter for iter in out])                                              # ['bool', True, 1]