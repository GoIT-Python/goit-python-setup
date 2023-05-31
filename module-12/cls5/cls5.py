import csv

# with open('data.csv', 'w', newline='') as fh:
#     writer = csv.writer(fh)
#     writer.writerow([1, 2, 3])
#     writer.writerow([5, 6, None, 8])
#
# with open('test.csv', 'r', newline='') as fh:
#     reader = csv.reader(fh)
#     for row in reader:
#         print(', '.join(row))

with open('names.csv', 'w', newline='') as fh:
    field_names = ['first_name', 'last_name']
    writer = csv.DictWriter(fh, fieldnames=field_names)
    writer.writeheader()
    writer.writerow({'first_name': 'Jack', 'last_name': 'White'})
    writer.writerow({'first_name': 'John', 'last_name': 'Travolta'})

with open('test.csv', newline='') as fh:
    reader = csv.DictReader(fh)
    for row in reader:
        print(row)
