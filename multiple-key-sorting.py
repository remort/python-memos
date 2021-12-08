from random import randint
from datetime import datetime, timedelta

a = [{'is_available': 0 if x % 2 == 0 else 1, 'id': randint(0, 100)} for x in range(1, 11)]
b = [{'is_available': True if x % 2 == 0 else False, 'id': randint(0, 100)} for x in range(1, 11)]
sorted(b, key=lambda i: (not i['is_available'], i['id'])) 


c = [{'is_available': True if x % 2 == 0 else False, 'date': str(datetime.now() + timedelta(minutes=randint(0,100)))} for x in range(1, 11)]
sorted(c, key=lambda i: (i['is_available'], i['date']))

c = [{'k1': bool(randint(0,1)), 'k2': None if randint(0,10) % 2 else randint(0,10), 'k3': None if not randint(0,10) % 4 else randint(0,10)} for x in range(0, 20)]
sorted(col, key=lambda i: (not i['k1'], i['k2'] or i['k3'] or 0))
