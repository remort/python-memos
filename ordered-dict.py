# append/modify collection's items regardless their existence
country_codes = {'africa': ['zm', 'zw', 'eh'], 'asia': ['ye', 'uz'], 'europe': ['ua', 'uk']}
additianal_codes = {'africa': 'ug', 'asia': 'vn', 'europe': 'al', 'south_america': 'ar', 'north america': 'ca'}

# the usual way
for k, v in additianal_codes.items():
    if k in country_codes:
        country_codes[k].append(v)
    else:
        country_codes[k] = [v]

# the OrderedDict `setdefault` way
country_codes = OrderedDict({'africa': ['zm', 'zw', 'eh'], 'asia': ['ye', 'uz'], 'europe': ['ua', 'uk']})
additianal_codes = {'africa': 'ug', 'asia': 'vn', 'europe': 'al', 'south_america': 'ar', 'north america': 'ca'}

for k, v in additianal_codes.items():
    country_codes.setdefault(k, []).append(v)
