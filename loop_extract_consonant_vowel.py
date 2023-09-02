sentence = 'Zvuk řeči je produkován poměrně otevřenou konfigurací vokálního traktu'
vowels = "eyuioa"
final = {"Vowels": 0, "Consonants": 0}
for letter in sentence:
    if not letter.isalpha():
        continue
    elif letter in vowels:
#        final["Vowels"] = final["Vowels"] + 1
        final["Vowels"] +=1
    else:
#        final["Consonants"] = final["Consonants"] + 1
        final["Consonants"] +=1
        
#print("Consonants:", final["Consonants"], "|", "Vowels:", final["Vowels"])
print(" | ".join([f"{key}: {value}" for key, value in final.items()]))
# BOOL
def fc(z):
    x = 'eyuioa'
#    print([f"{z} - {z in x}" for z in z if z in x])                       # ['u - True', 'e - True', 'i - True', ...]
    print([f"{z} - {z in x}" if z in x else f"{z} - {z in x}" for z in z]) # ['Z - False', 'v - False', 'u - True', ...]
fc('Zvuk řeči je produkován poměrně otevřenou konfigurací vokálního traktu')
# GENERATOR
z = 'Zvuk řeči je produkován poměrně otevřenou konfigurací vokálního traktu'
x = 'eyuioa'
w = (f"{z} - {z in x}" if z in x else f"{z} - {z in x}" for z in z)
print(next(w))                                                             # Z - False
print(next(w))                                                             # v - False
print(next(w))                                                             # u - True
print(next(w))                                                             # k - False
# or
z = 'Zvuk řeči je produkován poměrně otevřenou konfigurací vokálního traktu'
x = 'eyuioa'
def fung():
    for z in z:
        yield z
gen = (f"{z} - {z in x}" if z in x else f"{z} - {z in x}" for z in z)
print(next(gen))                                                           # Z - False
print(next(gen))                                                           # v - False
print(next(gen))                                                           # u - True
# or
z = 'Zvuk řeči je produkován poměrně otevřenou konfigurací vokálního traktu'
x = 'eyuioa'
def fung():
    for z in z:
        yield z
gen = (f"{z} - {z in x}" if z in x else f"{z} - {z in x}" for z in z)
itr = 0
while itr < len(z):                                                        # Z - False
    print(next(gen))                                                       # v - False
    itr += 1                                                               # u - True ...