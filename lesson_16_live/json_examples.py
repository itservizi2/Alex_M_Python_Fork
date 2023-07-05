import json

list_of_items = [a for a in range(100)]
with open('numbers.json', 'w') as file:
    json.dump(list_of_items, file)
