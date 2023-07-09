from datetime import datetime

HOUR_FORMAT = '%H:%M'
DATE_FORMAT = '%d/%m/%Y'

# time = input('Time in 24 hour format H:M')
# parsed_time = datetime.strptime(time, '%H:%M')
# print(parsed_time.strftime('%I:%M %p'))
#
# time = input('Time in 24 hour format H:M AM/PM')
# parsed_time = datetime.strptime(time, '%I:%M %p')
# print(parsed_time.strftime('%H:%M'))

date = input('Date in dd/mm/yyyy')
parsed_time = datetime.strptime(date, DATE_FORMAT)
print(parsed_time)
