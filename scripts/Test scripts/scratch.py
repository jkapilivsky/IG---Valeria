
value = '22.3m'

if 'k' in value:
    if '.' in value:
        value = value + '00'
    else:
        value = value + '000'

if 'm' in value:
    if '.' in value:
        value = value + '00000'
    else:
        value = value + '000000'

value = value.replace('k', '')
value = value.replace('m', '')
value = value.replace('.' , '')
print(int(value))