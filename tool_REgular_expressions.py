# findall	Возвращает список со всеми совпадениями
# search	Возвращает объект Match, если в строке есть совпадение
# split	Возвращает список, из строки, которую разделили по шаблону
# sub	Заменяет совпадение по шаблону, на заданную строку

# .span() возвращает кортеж, содержащий начальную и конечную позиции совпадения.
# .string возвращает строку, переданную в функцию.
# .group() возвращает часть строки, где было совпадение

# []	Содержит символы для поиска вхождений	[a-m]
# \	Сигнализирует о специальном символе (также может использоваться для экранирования специальных символов)	\d
# .	Любой символ, кроме новой строки (\n)	“he…o”
# ^	Строка начинается с	“^hello”
# $	Строка заканчивается	“world$”
# *	0 и более вхождений	“aix*”
# +	1 и более вхождений	“aix+”
# {}	Указанное количество вхождений	“al{2}”
# |	Или	“falls|stays”
# ()	Группирует шаблон

# \A	Ищет символы в начале строки	“\AThe”
# \b	Ищет символы в начале или конец слова, в зависимости от расположения	r»\bain» r»ain\b»
# \B	Ищет символы которые находятся НЕ в начале или конце строки	r»\Bain» r»ain\B»
# \d	Ищет совпадения с числами 0-9	“\d”
# \D	Ищет совпадение, где строка не содержит числа	“\D”
# \s	Ищет совпадение с символом пробела	“\s”
# \S	Ищет совпадение, где строка НЕ содержит пробел	“\S”
# \w	Ищет совпадение, где строка содержит буквы, цифры или символ по подчеркивания (_)	“\w”
# \W	Ищет совпадение, где строка НЕ содержит буквы, цифры или символ по подчеркивания (_)	“\W”
# \Z	Ищет символы в конце строки	“Spain\Z”

# [arn]	Возвращает совпадение, в котором присутствует один из указанных символов (a, r или n)
# [a-n]	Возвращает совпадение для с символом нижнего регистра в алфавитном порядке между a и n, включая их
# [^arn]	Возвращает совпадение для любого символа, КРОМЕ а, r и n
# [0123]	Возвращает совпадение, в котором присутствует любая из указанных цифр (0, 1, 2 или 3)
# [0-9]	Возвращает совпадение с любой цифрой от 0 до 9
# [0-5][0-9]	Возвращает совпадение с любыми двузначными числами от 0 до 59
# [a-zA-Z]	Возвращает совпадение с любым символом английского алфавита между a и z, включая строчные буквы и прописные
# [а-яА-ЯёЁ]	Возвращает совпадение с любым символом русского алфавита между а и я, включая строчные буквы и прописные
# [+]	В комбинациях символы +, *, ., |, (), $,{} не имеют особенного значения, поэтому [+]: будет искать любой + в строке

f4 = "'Baisers volés', 1968, 'colour', 'François Truffaut', 'Jean-Pierre Léaud'"
import re
print(re.search("A", f4))                           # None
print(re.search("f", f4))                           # <re.Match object; span=(46, 47), match='f'>
print(re.search("f*", f4))                          # <re.Match object; span=(0, 0), match=''>
print(re.search("f*", f4).span())                   # (0, 0)
print(re.search("f*", f4).string)                   # 'Baisers volés', 1968, 'colour', 'François Truffaut', 'Jean-Pierre Léaud'
print(re.search("f*", f4).group())                  # 
print(re.search("[1-9]+", f4).group())              # 1968
print(re.search("[1-8]+", f4).group())              # 1
print(re.search("[1-8]*", f4).group())              # 
print(re.search("[1-8]+", f4).span())               # (17, 18)
print(re.search("f+", f4))                          # <re.Match object; span=(46, 48), match='ff'>
print(re.search("f+", f4).span())                   # (46, 48)
print(re.search("f+", f4).string)                   # 'Baisers volés', 1968, 'colour', 'François Truffaut', 'Jean-Pierre Léaud'
print(re.search("f+", f4).group())                  # ff
print(re.findall("f", f4))                          # ['f', 'f']
print(re.findall("[f]", f4))                        # ['f', 'f']
print(re.findall("f*", f4))                         # ['', '', '', '' ... 'ff' ...
print(re.findall("f+", f4))                         # ['ff']
print(re.findall("[f*]", f4))                       # ['f', 'f']
print(re.findall("[f+]", f4))                       # ['f', 'f']
print(re.findall("[a-f*]", f4))                     # ['a', 'e', 'c', 'a', 'f', 'f', 'a', 'e', 'a', 'e', 'e', 'a', 'd']
print(re.findall("\d", f4))                         # ['1', '9', '6', '8']
print(re.findall("\d*", f4))                        # ['', '', '', '', '', ...
print(re.findall("\d+", f4))                        # ['1968']
print(re.findall("^'B", f4))                        # ["'B"]
print(re.split("\d+", f4, maxsplit=17))             # ["'Baisers volés', ", ", 'colour', ...
print(re.split(".", f4, maxsplit=3))                # ['', '', '', "isers volés', 1968, ...
print(re.sub("\d+", '2020', f4, count=0))           # 'Baisers volés', 2020, 'colour', ...
print(re.sub("\d*", '2020', f4, count=0))           # 2020'2020B2020a2020i2020s2 ...
print(re.sub("a+", '#', f4, count=4))               # 'B#isers volés', 1968, 'colour', 'Fr#nçois Truff#ut', 'Je#n-Pierre Léaud'
