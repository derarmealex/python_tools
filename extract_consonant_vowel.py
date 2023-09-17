z = 'Zvuk řeči je produkován poměrně otevřenou konfigurací vokálního traktu'
x = "eyuioa"

final = {"Vowels": 0, "Consonants": 0}
for letter in z:
    if not letter.isalpha():
        continue
    elif letter in x:
        final["Vowels"] += 1
    else:
        final["Consonants"] += 1

print("Vowels:", final["Vowels"], "|", "Consonants:", final["Consonants"])   # Vowels: 21 | Consonants: 41
print(" | ".join([f"{key}: {value}" for key, value in final.items()]))       # Vowels: 21 | Consonants: 41


# BOOL
def fc(z):
    print([f"{z} - {z in x}" for z in z if z in x])                          # ['u - True', 'e - True', 'i - ...
    print([f"{z} - {z in x}" if z in x else f"{z} - {z in x}" for z in z])   # ['Z - False', 'v - False', 'u -  ...


fc(z)
# GENERATOR
gen = (f"{z} - {z in x}" if z in x else f"{z} - {z in x}" for z in z)
print(next(gen))                                                               # Z - False
print(next(gen))                                                               # v - False
print(next(gen))                                                               # u - True
print(next(gen))                                                               # k - False


# or
def fungus():
    for z in z:
        yield z


gen = (f"{z} - {z in x}" if z in x else f"{z} - {z in x}" for z in z)
print(next(gen))                                                             # Z - False
print(next(gen))                                                             # v - False
print(next(gen))                                                             # u - True


# or
def fungus():
    for z in z:
        yield z


gen = (f"{z} - {z in x}" if z in x else f"{z} - {z in x}" for z in z)
itr = 0
while itr < len(z):                                                          # Z - False
    print(next(gen))                                                         # v - False
    itr += 1                                                                 # u - True ...
