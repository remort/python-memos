CONF = {
    'version': '1.0',
    'modules': {
        'logger': {
            'enabled': True,
            'level': 'DEBUG'
        },
        'calc': {
            'enabled': False,
            'mode': 'advanced',
        }
    }
}

print(f'CONF in {__name__}: {CONF}')
