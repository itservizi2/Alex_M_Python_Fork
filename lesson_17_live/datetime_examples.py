from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

print(
    datetime.now(tz=timezone(timedelta(hours=3)))
)
print(
    datetime.now(tz=ZoneInfo("America/New_York"))
)

maine = datetime(2023, 7, 8, 20, 30)
acum = datetime.now()

diferenta = maine - acum

print(diferenta)
print(diferenta.seconds)
print(diferenta.days)
print(diferenta.microseconds)
print(diferenta.total_seconds() // 60 // 60)

timp_in_15_mine = datetime.now() + timedelta(hours=1, minutes=15)
timp_acum = datetime.now()

print(timp_acum > timp_in_15_mine)
print(timp_acum < timp_in_15_mine)
print(timp_acum == timp_in_15_mine)
print(timp_in_15_mine - timp_acum)
