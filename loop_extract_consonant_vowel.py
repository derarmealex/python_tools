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
