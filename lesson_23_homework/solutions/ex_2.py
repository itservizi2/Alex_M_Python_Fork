import functools
import json
from dataclasses import dataclass


@functools.total_ordering
@dataclass
class CurrencyConversion:
    from_currency: str
    to_currency: str
    rate: float
    inverse_rate: float
    code: str
    name: str

    def __eq__(self, other):
        if not isinstance(other, CurrencyConversion):
            return NotImplemented
        return self.rate == other.rate

    def __lt__(self, other):
        return self.rate < other.rate


class CurrencyConversionService:
    def __init__(self, rates, base_currency='MDL'):
        self.base_currency = base_currency
        self.conversions = []
        self.rates = rates
        self.load_conversions()

    def load_conversions(self):
        for rate_info in self.rates:
            rate = rate_info['rate']
            name = rate_info['name']
            cc = CurrencyConversion(
                from_currency=self.base_currency,
                to_currency=rate_info['code'],
                rate=rate,  # Invert the rate since it's from_currency to base currency
                code=rate_info['code'],
                name=name,
                inverse_rate=rate_info['inverseRate']
            )
            self.conversions.append(cc)
        self.conversions.sort()

    def is_conversion_supported(self, from_currency, to_currency):
        return any(cc.from_currency == from_currency and cc.to_currency == to_currency for cc in self.conversions)

    def convert(self, from_currency, to_currency, amount):
        is_inverse = False
        if to_currency == self.base_currency:
            is_inverse = True
        from_currency, to_currency = to_currency, from_currency
        if not self.is_conversion_supported(from_currency, to_currency):
            raise ValueError(f"Conversion from {from_currency} to {to_currency} not supported")
        conversion = [c for c in self.conversions if c.from_currency == from_currency and c.to_currency == to_currency]
        rate = conversion[0].rate if not is_inverse else conversion[0].inverse_rate
        return round(amount * rate, 2)


if __name__ == "__main__":

    with open("conversion_rates.json", "r") as f:
        rates: dict = json.load(f)

    # Get base currency
    base_currency = list(rates.keys())[0]

    # Get inner dict
    inner_dict = rates[base_currency]

    # Build flattened rates dict
    rates: list = list(rates.values())

    ccs = CurrencyConversionService(rates, "MDL")

    print("Possible currency conversions:")
    for cc in ccs.conversions:
        print(cc)

    from_currency = input("Enter currency to convert from (MDL): ")
    if from_currency.upper() == ccs.base_currency:
        to_currency = input("Enter currency to convert to: ")
        amount = float(input(f"Enter amount in MDL to convert to {to_currency}: "))
        converted = ccs.convert(ccs.base_currency, to_currency, amount)
        print(f"{amount} MDL is equal to {converted} {to_currency}")
    else:
        to_currency = "MDL"
        amount = float(input(f"Enter amount in {from_currency} to convert to MDL: "))
        converted = ccs.convert(from_currency, ccs.base_currency, amount)
        print(f"{amount} {from_currency} is equal to {converted} MDL")
