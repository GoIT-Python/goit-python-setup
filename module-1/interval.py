interval = int(input("Input time interval in seconds: "))
hours = interval // 3600
minutes = (interval - hours * 3600) // 60
seconds = (interval - hours * 3600) % 60

print(f"hours: {hours} \nminutes: {minutes} \nseconds: {seconds}")
