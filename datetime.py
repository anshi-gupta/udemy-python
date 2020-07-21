import datetime
mytime = datetime.time(2, 20)
print(f"Hour: {mytime.hour}")
print(f"Minute: {mytime.minute}")
print(f"Random time: {mytime}")
print("\n")

time_in_ms = datetime.time(4, 20, 14, 30)
print(f"Time in millisecond: {time_in_ms}")
print("\n")

today = datetime.date.today()
print(f"Today's date: {today}")
print(f"Year: {today.year}")
print(f"Month: {today.month}")
print(f"Day: {today.day}")
print("\n")
print(today.ctime())

# For both date and time
from datetime import datetime
mydatetime = datetime(2025, 5, 22, 8, 30)
print("\n")
print(f"Given date and time {mydatetime}")

# Change the data(here: year)
mydatetime = mydatetime.replace(year = 2022)
print("\n")
print(f"The year was changed to {mydatetime.year}")
print(f"Changed date and time {mydatetime}")

# Date difference
print("\n")
from datetime import date
date1 = date(2022, 12, 14)
date2 = date(2021, 12, 14)
print(f"Date1 : {date1}")
print(f"Date2 : {date2}")
result = date1 - date2
a = type(result)
print(f"Type: {a}")
print(f"Total days difference between date1 and date2 is {result.days}")

# Both date time
print("\n")
datetime1 = datetime(2022, 12, 14, 22, 10)
datetime2 = datetime(2021, 12, 14, 12, 10)
print(f"Datetime1 : {datetime1}")
print(f"Datetime2 : {datetime2}")
r = datetime1 - datetime2
print(f"Total days and time difference between datetime1 and datetime2 is {r}")
print(f"Total Seconds is {r.total_seconds()}")
print(f"Second difference is {r.seconds}")