from datetime import datetime
import time

# print(time.time())

current_time = datetime.now()
print(current_time)
# print(current_time.microsecond)
print(current_time.date())
print(current_time.time())

custom_dt = datetime(year=1970, month=4, day=22)
print(custom_dt)
print(custom_dt.weekday())

custom_dt1 = datetime(year=1970, month=4, day=22)
custom_dt2 = datetime(year=1992, month=4, day=25)

result=custom_dt2-custom_dt1
print(result.days)




