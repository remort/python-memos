from a import CONF

print(f'CONF in {__name__} before modifying: {CONF}')

CONF['version'] = '2.0'
CONF['modules']['logger']['level'] = 'INFO'

print(f'CONF in {__name__} after modifying: {CONF}')
