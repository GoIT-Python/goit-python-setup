from datetime import datetime, timedelta

now = datetime.now()

# print(now)
# print(now.strftime("%a %d %B %Y %H:%M"))  # Tuesday 07 January 2020


s = "10 January 2020"
custom_dt = datetime.strptime(s, "%d %B %Y")
# print(custom_dt)

print(custom_dt.timestamp())
#
# print(datetime.fromtimestamp(custom_dt.timestamp()))

d1 = datetime(year=99, month=1, day=1, hour=0)
print(d1)  # 2012-01-07 14:00:00
print(d1.timestamp())  # 2012-01-07 14:00:00
