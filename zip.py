# modify items of one collection by corresponding items of another.
a=({'name': 'John', 'age': 42}, {'name': 'Pete', 'age': 33})
b=(10, 20)

# the usual way
for index, item in enumerate(a):
    item['age'] = b[index]

# change mutable iterable elements while walk over them with zip()
for x, y in zip(a,b):
    x['age'] = y

# unzip of flat iterators. use .pop() instead next() for list
a = (x for x in range(105))
list((tuple(next(a) for x in range(10)) for y in range(10))) + [x for x in (tuple(a),) if x]

# 10x10 matrix has been flatten by zip()
list(zip(*([x for x in range(100)][i::10] for i in range(10))))
