import json

with open('currency.json') as file:
    currency_data = json.load(file)

amount_lei = float(input('Amount'))
rata_de_schimb = currency_data['usd']['rate']
result = amount_lei * rata_de_schimb
print(f"{amount_lei} in MDL va fi {result:.2f} USD")

try:
    with open('history_2.json', 'r') as hist:
        history_data = hist.read()
except Exception:
    history_data = ''

print(history_data)

history_data += str(dict(from_amount=amount_lei, to_amount=result, currency='USD'))

with open('history_2.json', 'w') as hist:
    hist.write(history_data)
