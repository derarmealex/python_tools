# r 	Открыть файл для чтения. (используется по умолчанию)
# t 	Открыть файл в текстовом режиме. (используется по умолчанию)
# w 	Открыть файл для записи. Создает новый файл, если он не существует, или удаляет содержимое файла, если он существует.
# a 	Открыть файл для добавления данных в конец файла без удаления текущего содержимого. Создает новый файл, если он не существует.
# x 	Открыть файл для эксклюзивного создания. Если файл уже существует, операция завершится неудачно.
# b 	Открыть файл в двоичном режиме.
# + 	Открыть файл для обновления (чтение и запись).

# close() 	                Закрывает открытый файл. Ничего не происходит, если файл уже закрыт.
# detach() 	                Отделяет базовый двоичный буфер от TextIOBase и возвращает его.
# fileno() 	                Возвращает целое число файла (файловый дескриптор).
# flush() 	                Очищает буфер записи в файловом потоке.
# isatty() 	                Возвращает True, если поток файлов является интерактивным.
# read(n) 	                Считывает не более n символов из файла. Выполняет чтение до конца файла, если n является отрицательным или None.
# readable() 	            Возвращает True, если из файлового потока можно считать данные.
# readline(n=-1) 	        Считывает и возвращает одну строку из файла. Считывает не более n байт, если указано.
# readlines(n=-1) 	        Считывает и возвращает список строк из файла. Считывает не более n байт/символов, если указано.
# seek(offset,from=SEEK_SET) Изменяет позицию файла на offset байтов, относительно from (start, current, end).
# seekable() 	            Возвращает True, если файловый поток поддерживает произвольный доступ.
# tell() 	                Возвращает целое число, представляющее текущую позицию файлового объекта.
# truncate(size=None) 	    Изменяет размер файлового потока до size байт. Если размер не указан, размер изменяется относительно текущего местоположения.
# writable() 	            Возвращает True, если в файловый поток можно выполнить запись.
# write(s) 	                Записывает строку (s) в файл и возвращает количество записанных символов.
# writelines(lines)         Записывает список строк (lines) в файл.

if __name__ == "__main__":
    file = open("tool_files_txt.txt")               # = file1 = open("tool_files_txt.txt", "r")
    file2 = open("tool_files_txt.txt", "r+b")
    file3 = open("tool_files_txt2.txt")

    read_content = file.read()
    print(read_content)
    file.close()
    print("\n")
    # or
    try:
    #    read_content = file.read()
        print(read_content)
    except Exception as e:
        print(e)
    finally:
        file.close()
    print("\n")
# RECOMMENDED WAY TO OPEN
    with open("tool_files_txt.txt", "r") as file:
        read_content = file.read()
        print(read_content)
# WRITE ADDITIONAL TEXT AFTER THE END (IF IS NOT FILE WILL BE CREATED)
    with open("tool_files_txt2.txt", "r+") as file:
        print(file.read(), "\n")
        file.write("\n\nAlexander Blok")                # called file will be edited right away!
# or
#        print("\n\nAlexander Blok", file=file)
    #    print(file.read())                             # changes won't be visible until reopening
    file = open("tool_files_txt2.txt")
    read_content = file.read()
    print(read_content)
    file.close()
# REWRITE FILE (IF IS NOT FILE WILL BE CREATED)
    with open("tool_files_txt_draft.txt", "w+") as file: # file created
        file.write("trying\nanother one")               # file edited
# EXCLUSIVE CREATING
    with open("tool_files_txt_draft.txt", "x") as file:
        file.write("trying\nanother one")               # FileExistsError: [Errno 17] File exists: 'tool_fil ...
# READABILITY
file = open("tool_files_txt.txt")
file4 = open("tool_files_jpg.jpg")
file5 = open("C:\\Users\\alexa\\Desktop\\Dingir304.pdf")
print(file.readable())                                  # True
print(file4.readable())                                 # True
print(file5.readable())                                 # True
