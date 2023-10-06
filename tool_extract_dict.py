employees = {
 'employee01': {'Name': 'Marek', 'Surname': 'Parek', 'Email': 'marek.parek@gmail.com'},
 'employee02': {'Name': 'Matous', 'Surname': 'Svatous', 'Email': 'matous.svatous@gmail.com'},
 'employee03': {'Name': 'Anna', 'Surname': 'Rana', 'Email': 'anna.rana@gmail.com'},
 'employee04': {'Name': 'Alex', 'Surname': 'Brown', 'Email': 'alex.brown@rhosgobel.com'}
            }

print([new for new in employees])                  # ['employee01', 'employee02', 'employee03', 'employee04']
print([new for new in employees for new in new])   # ['e', 'm', 'p', 'l', 'o', ...
val = employees.values()                           # dict_values([{'Name': 'Marek', 'Surname': 'Parek', ...
print([new for new in val])                        # [{'Name': 'Marek', 'Surname': 'Parek', ...
print([new for new in val for new in new])         # ['Name', 'Surname', 'Email', 'Name', ...
print([new for new in val if new == "Email"])      # ['Email', 'Email', 'Email', 'Email']
print([new[post] for new in val for post in new])  # ['Marek', 'Parek', 'marek.parek@gmail.com', 'Matous', ...

print([person[post] for person in val for post in person if post == "Email"])
# ['marek.parek@gmail.com', 'matous.svatous@gmail.com', 'anna.rana@gmail.com', 'alex.brown@rhosgobel.com']
# or
post = []
for person in employees.values():
    post.append(person["Email"])
print(post)
# ['marek.parek@gmail.com', 'matous.svatous@gmail.com', 'anna.rana@gmail.com', 'alex.brown@rhosgobel.com']
