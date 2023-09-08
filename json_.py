#Python	JSON
#dict	Object
#list	Array
#tuple	Array
#str	String
#int	Number
#float	Number
#True	true
#False	false
#None	null

# JSON to Python
import json
x = '{"name":"Viktor", "age":30, "city":"Minsk"}'
# парсинг x:
y = json.loads(x)
# результатом будет словарь Python:
print(y)
# Python to JSON
import json
x = {"name": "Viktor",
"age": 30,
"city": "Minsk"}
# конвертируем в JSON: 
y = json.dumps(x)
print(y)
# Cyrillic
import json
x = {"name": "Виктор"}
y = {"name": "Виктор"}
print(json.dumps(x))                                # {"name": "\u0412\u0438\u043a\u0442\u043e\u0440"}
print(json.dumps(y, ensure_ascii=False))            # {"name": "Виктор"}