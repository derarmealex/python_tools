import calendar
print(calendar.__doc__)
help(calendar)
calendar.setfirstweekday(0)
calendar.Calendar(firstweekday=0)
x = calendar.calendar(2023)
print(x)
z = calendar.Calendar(2024)
print(z)                                                # <calendar.Calendar object at 0x000002F2F0944C90>
print(calendar.month(2024,1))
print(calendar.month(2023, 8))
print(calendar.weekday(2023,8,13))
print(z.getfirstweekday())
print(x.monthdatescalendar(2023,8))
