from collections import defaultdict

dd = defaultdict(list)

print(dd['1'])

dict().get('key', list())

dd['1'].append(12)
dd['2'].append(13)
dd['2'].append(14)
dd['2'] = 1
# Produce eroare
# dd['2'].append(2)

print(dd)

users_dict = dict()

users_dict['1'] = dict(username='marius')
print(users_dict)
