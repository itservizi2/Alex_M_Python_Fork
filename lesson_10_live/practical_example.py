cos = [
    {
        'produs_id': 1,
        'quantity': 10
    },
    {
        'produs_id': 3,
        'quantity': 10
    },
    {
        'produs_id': 2,
        'quantity': 10
    },
    {
        'produs_id': 1,
        'quantity': 10
    },
    {
        'produs_id': 1,
        'quantity': 10
    },
    {
        'produs_id': 2,
        'quantity': 10
    },
    {
        'produs_id': 10,
        'quantity': 10
    },
]

totaluri = dict()

for comanda in cos:
    prod_id = comanda['produs_id']
    totaluri[prod_id] = totaluri.get(prod_id, 0) + comanda['quantity']

print(totaluri)

for prod_id, total in totaluri.items():
    print(f"Trebuie sa comand {prod_id} in cantintatea {total}")

print(list(totaluri.items()))

person = {'name': 'Marius',
          'country': {
              'name': 'Moldova',
              'shortname': 'MD'
          }
          }

print(person.get('country').get('name'))
print(person['country']['shortname'])
