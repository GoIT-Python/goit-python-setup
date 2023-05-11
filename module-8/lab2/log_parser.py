from datetime import datetime

# 07.05.2023, 14:00:49 - INFO - Starts module

log_times = []
logs = []

with open("logs.txt", "r") as file:
    # logs = file.readlines()
    # print(logs)

    for line in file.readlines():
        logs.append(line)
        time = datetime.strptime(line.split(" - ")[0], "%d.%m.%Y, %H:%M:%S")
        log_times.append(time)

start_date = input("Start time in format: (dd.mm.YYYY HH:MM:SS): ")
start_date = datetime.strptime(start_date, "%d.%m.%Y, %H:%M:%S")
end_date = input("End time in format: (dd.mm.YYYY HH:MM:SS): ")
end_date = datetime.strptime(end_date, "%d.%m.%Y, %H:%M:%S")

for i, log_time in zip(logs, log_times):
    if start_date < log_time < end_date:
        print(logs)
