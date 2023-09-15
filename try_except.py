try:
    f = open("E:\music\Various Artists\Bob Kerrey-The Band Played Waltzing Matilda.mp3")
#    f.write("Lorum Ipsum")
    print("File found!")
except NameError:
    print("Variable doesn't exist!")
except FileNotFoundError:
    print("File not found!")
except:
    print("Something went wrong while writing to the file")
else:
    print("No errors found")
finally:
    f.close()
