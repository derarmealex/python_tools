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