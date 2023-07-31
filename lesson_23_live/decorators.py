from datetime import datetime, timedelta


class Date:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"Date:{self.day}/{self.month}/{self.year}"

    @staticmethod
    def is_date_valid(date: str):
        pass

    @classmethod
    def from_string(cls, date_string: str):
        "Avand o data de formatul 18-02-2012"
        day, month, year = map(int, date_string.split('-'))
        date_object = cls(day, month, year)
        return date_object

    @classmethod
    def today(cls):
        today = datetime.now().date()
        return cls(day=today.day, month=today.month, year=today.year)

    @staticmethod
    def get_today_date():
        today = datetime.now().date()
        return Date(day=today.day, month=today.month, year=today.year)

    @classmethod
    def tomorrow(cls):
        obj = cls.today()
        obj.day += 1
        return obj


class DateWithTZ(Date):

    def __init__(self, *args, tz='UTC+0', **kwargs):
        super().__init__(*args, **kwargs)
        self.tz = tz

    def __str__(self):
        return f"{super().__str__()}:{self.tz}"

    @classmethod
    def today(cls):
        today = datetime.now().date()
        return cls(day=today.day, month=today.month, year=today.year, tz='UTC:+)2')

    @staticmethod
    def get_today_date():
        today = datetime.now().date()
        return DateWithTZ(day=today.day, month=today.month, year=today.year)


print(Date.get_today_date())

print(DateWithTZ.today())
print(DateWithTZ.get_today_date())


class DateUtils:

    @staticmethod
    def get_tomorrow():
        return datetime.now() + timedelta(days=1)

    @staticmethod
    def get_next_sunrise():
        return


