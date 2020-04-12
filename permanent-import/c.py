from copy import deepcopy

from a import CONF


print(f'CONF in {__name__}: {CONF}')

mod_conf = deepcopy(CONF)
mod_conf['version'] = '3.0'
mod_conf['modules']['logger']['level'] = 'TRACE'
