dispoinibl = ['paine', 'mar']

cos = ['mar', 'banana', 'paine']

checkout = []

for produs in cos:
    if produs not in dispoinibl:
        # Nu are sens sa procesam
        continue
    # Procesam
    print(f'Checking out {produs}')
    checkout.append(produs)

print(checkout)
