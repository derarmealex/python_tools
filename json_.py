# Python    JSON
# dict	    Object
# list	    Array
# tuple	    Array
# str	    String
# int	    Number
# float     Number
# True	    true
# False 	false
# None	    null

# JSON to Python
import json
x = '{"name": "Viktor", "age": 30, "city": "Minsk"}'
print(x)                                              # {"name": "Viktor", "age": 30, "city": "Minsk"}
x = json.loads(x)
print(x)                                              # {"name": "Viktor", "age": 30, "city": "Minsk"}
# Python to JSON
x = {
    "name": "Viktor",
    "age": 30,
    "city": "Minsk"
    }
print(x)                                              # {'name': 'Viktor', 'age': 30, 'city': 'Minsk'}
x = json.dumps(x)
print(x)                                              # {'name': 'Viktor', 'age': 30, 'city': 'Minsk'}
# Cyrillic
x = {"name": "Виктор"}
y = {"name": "Виктор"}
print(json.dumps(x))                                  # {"name": "\u0412\u0438\u043a\u0442\u043e\u0440"}
print(json.dumps(y, ensure_ascii=True))               # {"name": "\u0412\u0438\u043a\u0442\u043e\u0440"}
print(json.dumps(y, ensure_ascii=False))              # {"name": "Виктор"}
