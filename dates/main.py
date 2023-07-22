from datetime import datetime
from datetime import date

print("====================")
print("dates")
print("====================")

print(datetime.now())
print(datetime.now().year)
print(datetime.now().month)
print(datetime.now().day)
print(datetime.now().hour)
print(date.today())

print("====================")
print("Formatting dates")
print("====================")

today = date.today().strftime("%d/%m/%y")
now = datetime.now()

print(today)
print(now.strftime("%d-%B-%y | %H:%M:%S"))
print(now.strftime("%d-%b-%y | %H:%M:%S"))
