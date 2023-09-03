#%a	День недели, короткий вариант	Wed
#%A	Будний день, полный вариант	Wednesday
#%w	День недели числом 0-6, 0 — воскресенье	3
#%d	День месяца 01-31	31
#%b	Название месяца, короткий вариант	Dec
#%B	Название месяца, полное название	December
#%m	Месяц числом 01-12	12
#%y	Год, короткий вариант, без века	18
#%Y	Год, полный вариант	2018
#%H	Час 00-23	17
#%I	Час 00-12	05
#%p	AM/PM	PM
#%M	Минута 00-59	41
#%S	Секунда 00-59	08
#%f	Микросекунда 000000-999999	548513
#%z	Разница UTC	+0100
#%Z	Часовой пояс	CST
#%j	День в году 001-366	365
#%U	Неделя числом в году, Воскресенье первый день недели, 00-53	52
#%W	Неделя числом в году, Понедельник первый день недели, 00-53	52
#%c	Локальная версия даты и времени	Mon Dec 31 17:41:00 2018
#%x	Локальная версия даты	12/31/18
#%X	Локальная версия времени	17:41:00
#%%	Символ “%”	%

import datetime
print(dir(datetime))
y = datetime.datetime(2024,1,1)
print(y.strftime("%Y-%m-%d %H:%M:%S %A %B"))    # 2024-01-01 00:00:00 Monday January
x = datetime.datetime.now()
print(x.day)
print(x.year)
print(x.month)
print(x.hour)
print(x.minute)
print(x.second)
print("Current date and time:")
y = datetime.date.today()
print(x)                                        # 2023-08-18 13:35:46.929428
print(y)                                        # 2023-09-03
print(z)                                        # 
print(x.strftime("%Y-%m-%d %H:%M:%S %A %B"))    # 2023-08-18 13:35:46 Friday August
#DELTA
x = datetime.datetime(2014,7,2)
y = datetime.datetime(2014,7,11)
print(abs(x - y))                               # 9 days, 0:00:00
print(abs(x - y).days)                          # 9
#or
from datetime import date
x = datetime.date(2014,7,2)
y = datetime.date(2014,7,11)
final = abs(x - y)                              # 9 days, 0:00:00
print(final.days)                               # 9

import time
print(time.ctime())                             # Fri Sep  1 18:29:07 2023
print(x.strftime('%c'))                         # Fri Sep  1 18:30:09 2023
print(x.strftime('%x'))                         # 08/18/23
print(x.strftime('%X'))                         # 13:35:46
print(x.strftime('%Z'))                         #
print(x.strftime('%W'))                         # 33
print(x.isocalendar().week)                     # 33