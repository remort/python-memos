# modify items of one collection by corresponding items of another.
a=({'name': 'John', 'age': 42}, {'name': 'Pete', 'age': 33})
b=(10, 20)

# the usual way
for index, item in enumerate(a):
    item['age'] = b[index]

# change mutable iterable elements while walk over them with zip()
for x, y in zip(a,b):
    x['age'] = y
