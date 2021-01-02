#!/usr/bin/python3

"""
Examples of short-circuiting evaluation in
'or', 'and', 'if-then-else', any() and all() python clauses.
The rest of python clauses are have strict evaluation.
"""


def cond_one():
    print('condition one is True')
    return True


def cond_two():
    print('condition two is False')
    return False


def cond_three():
    print('condition three is True')
    return True


def bool_(x):
    print(f'execute bool_ for {x}')
    return bool(x)


# 'and' and 'or' operators
cond_one() and cond_two() and cond_three()

cond_one() or cond_two() or cond_three()

# 'if-then-else' operator
print('First') if cond_one() else print('Second')  # 'First'
print('First') if cond_two() else print('Second')  # 'Second'

# all() and any() evaluate until false result is met, then exit early
any((x() for x in (cond_one, cond_two, cond_three)))
all((x() for x in (cond_one, cond_two, cond_three)))

any((bool_(x) for x in [0, 1, 2]))
all((bool_(x) for x in [1, 0, 2]))

any((bool_(x) for x in range(0, 3)))
all((bool_(x) for x in range(0, 3)))

# short-circuiting doesn't work for any() and all() with pre-defined collections
# because elements in collection are evaluated already.
any((cond_one(), cond_two(), cond_three()))
all((cond_one(), cond_two(), cond_three()))

# comparison operators works as `and` conditions internally
5 > 6 > cond_one()  # cond_one doesn't execute
7 > 6 > cond_one()  # cond_one executes
