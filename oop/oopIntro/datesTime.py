import datetime

date = datetime.date(2026, 1, 1) ## YYYY, MM, DD
today = datetime.date.today()

time = datetime.time(12, 30, 0) ## HH, MM, SS
now = datetime.datetime.now()

now = now.strftime("%H:%M:%S %m-%d-%Y") #changes display format, based off what I want
print(now)

target_datetime = datetime.datetime(2020, 1, 2, 12, 30, 1)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed")
else:
    print("Target date has not passed")
