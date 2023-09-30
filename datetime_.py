# %a	День недели, короткий вариант	Wed
# %A	Будний день, полный вариант	Wednesday
# %w	День недели числом 0-6, 0 — воскресенье	3
# %d	День месяца 01-31	31
# %b	Название месяца, короткий вариант	Dec
# %B	Название месяца, полное название	December
# %m	Месяц числом 01-12	12
# %y	Год, короткий вариант, без века	18
# %Y	Год, полный вариант	2018
# %H	Час 00-23	17
# %I	Час 00-12	05
# %p	AM/PM	PM
# %M	Минута 00-59	41
# %S	Секунда 00-59	08
# %f	Микросекунда 000000-999999	548513
# %z	Разница UTC	+0100
# %Z	Часовой пояс	CST
# %j	День в году 001-366	365
# %U	Неделя числом в году, Воскресенье первый день недели, 00-53	52
# %W	Неделя числом в году, Понедельник первый день недели, 00-53	52
# %c	Локальная версия даты и времени	Mon Dec 31 17:41:00 2018
# %x	Локальная версия даты	12/31/18
# %X	Локальная версия времени	17:41:00
# %%	Символ “%”	%

import time
x = time.ctime()
print(x)                                        # Fri Aug 18 13:35:46 2023

stg = "Hello, World!"                           # H
for i in range(0, len(stg)):                    ##e
    print(stg[i])                               ##l
    time.sleep(1)                               ##l ...

import datetime
print(datetime.__name__)
print(datetime.__doc__)
print(sorted(datetime.__dict__.keys()))
print(dir(datetime))
help(datetime)

y = datetime.datetime(2024, 1, 1)
print(y.strftime("%Y-%m-%d %H:%M:%S %A %B"))    # 2024-01-01 00:00:00 Monday January
x = datetime.datetime.now()
print(x.isocalendar().week)                     # 33
print(x.day)
print(x.year)
print(x.month)
print(x.hour)
print(x.minute)
print(x.second)
print(x.strftime('%c'))                         # Fri Aug 18 13:35:46 2023
print(x.strftime('%x'))                         # 08/18/23
print(x.strftime('%X'))                         # 13:35:46
print(x.strftime('%Z'))                         #
print(x.strftime('%W'))                         # 33
print(x)                                        # 2023-08-18 13:35:46.929428
print(x.strftime("%Y-%m-%d %H:%M:%S %A %B"))    # 2023-08-18 13:35:46 Friday August
z = datetime.date.today()
print(z)                                        # 2023-08-18
# DELTA
x = datetime.datetime(2014, 7, 2)
y = datetime.datetime(2014, 7, 11)
print(abs(x - y))                               # 9 days, 0:00:00
print(abs(x - y).days)                          # 9
# or
x = datetime.date(2014, 7, 2)
y = datetime.date(2014, 7, 11)
final = abs(x - y)                              # 9 days, 0:00:00
print(final.days)                               # 9
# or
from datetime import date
x = date(2014, 7, 2)
y = date(2014, 7, 11)
final = abs(x - y)                              # 9 days, 0:00:00
print(final.days)                               # 9
