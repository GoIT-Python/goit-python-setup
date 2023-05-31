import json

var = {
    'name': 'Jack',
    'age': 21,
    'brothers': ['Mark', 'Mike'],
    'single': True,
    '': None,
    'details': {''}
}

#
# data = {'name': 'Jack', 'age': 21, 'brothers': ['Mark', 'Mike']}
data = {'name': 'Jack', 'age': 21, 'brothers': ('Mark', 'Mike')}

# serialized = json.dumps(data)
# print(serialized)
#
# unpacked = json.loads(serialized)
# print(unpacked)

with open('data.json', 'w') as fh:
    json.dump(data, fh)

with open('data.json', 'r') as fh:
    unpacked = json.load(fh)

print(unpacked)
