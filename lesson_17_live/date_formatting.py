from datetime import datetime, timedelta

print(datetime.now())
print(datetime.now().strftime('%d/%m/%Y, %A, %b, %B'))
print(datetime.now().strftime('%d-%m-%y %H:%M Week %U %U'))

print((datetime.now() + timedelta(days=10)).strftime('%X'))
print((datetime.now() + timedelta(days=10)).strftime('%x'))
print((datetime.now() + timedelta(days=10)).strftime('%c'))
