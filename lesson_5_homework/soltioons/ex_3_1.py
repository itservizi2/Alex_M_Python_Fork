date_personale = list()
info_date = input("Ce date vrei, prin virgula").split(',')
for el in info_date:
    info = input(f"Introduceti {el}:")
    date_personale.append(info)

print(f"Lista cu date personale completata: {date_personale}")
