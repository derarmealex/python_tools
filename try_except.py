try:
    f = open("demofile.txt")                        # фал должен быть создан, иначе исключение FileNotFound
    f.write("Lorum Ipsum")
except NameError:
    print("Переменная x не существует")
except: 
    print("Что-то пошло не так при записи в файл")
else:  
    print("Ошибок не обнаружено")
finally:
    f.close()

my_file = open('Bob Kerrey-The Band Played Waltzing Matilda.mp3')
try:
   my_file.close()
   print("File found!")
except FileNotFoundError:
   print("File not found!")
