import json
from dataclasses import dataclass, field
from typing import Dict, List
import functools

@functools.total_ordering
@dataclass
class CurrencyConversion:
    from_currency: str
    to_currency: str
    rate: float
    name: str

    def __eq__(self, other):
        if not isinstance(other, CurrencyConversion):
            return NotImplemented
        return self.name == other.name and self.rate == other.rate

    def __lt__(self, other):
        return self.name < other.name

class CurrencyConversionService:
    def __init__(self, rates, base_currency='USD'):
        self.base = base_currency
        self.conversions = []
        self.rates = rates
        self.load_conversions()

    def load_conversions(self):
        for from_currency in self.rates:
            if from_currency != 'code':
                rate_info = self.rates[from_currency]
                if isinstance(rate_info, dict) and 'rate' in rate_info and 'name' in rate_info:
                    rate = rate_info['rate']
                    name = rate_info['name']
                    cc = CurrencyConversion(
                        from_currency=from_currency,
                        to_currency=self.base,
                        rate=1 / rate,  # Invert the rate since it's from_currency to base currency
                        name=name
                    )
                    self.conversions.append(cc)
                    # Add conversions from base currency to other currencies
                    for to_currency in self.rates:
                        if to_currency != 'code' and to_currency != from_currency:
                            rate_info_to = self.rates[to_currency]
                            if isinstance(rate_info_to, dict) and 'rate' in rate_info_to and 'name' in rate_info_to:
                                rate_to = rate_info_to['rate']
                                name_to = rate_info_to['name']
                                cc_to = CurrencyConversion(
                                    from_currency=self.base,
                                    to_currency=to_currency,
                                    rate=rate_to,
                                    name=name_to
                                )
                                self.conversions.append(cc_to)

        # Remove unsupported conversions
        supported_conversions = []
        for cc in self.conversions:
            try:
                self.convert(cc.from_currency, cc.to_currency, 1)  # Test if the conversion works
                supported_conversions.append(cc)
            except ValueError:
                pass

        self.conversions = supported_conversions
        self.conversions.sort()

    def is_conversion_supported(self, from_currency, to_currency):
        return any(cc.from_currency == from_currency and cc.to_currency == to_currency for cc in self.conversions)

    def convert(self, from_currency, to_currency, amount):
        if not self.is_conversion_supported(from_currency, to_currency):
            raise ValueError(f"Conversion from {from_currency} to {to_currency} not supported")

        conversion = [c for c in self.conversions if c.from_currency == from_currency and c.to_currency == to_currency]
        rate = conversion[0].rate
        return round(amount * rate, 2)


if __name__ == "__main__":

    with open("conversion_rates.json", "r") as f:
        rates = json.load(f)

    # Get base currency
    base_currency = list(rates.keys())[0]


    # Get inner dict
    inner_dict = rates[base_currency]

    # Build flattened rates dict
    rates = {}
    for currency, info in inner_dict.items():
        rates[currency] = info

    ccs = CurrencyConversionService(rates)

    print("Possible currency conversions:")
    for cc in ccs.conversions:
        print(cc)

    from_currency = input("Enter currency to convert from (MDL): ")
    if from_currency.upper() == "MDL":
        to_currency = input("Enter currency to convert to: ")
        amount = float(input(f"Enter amount in MDL to convert to {to_currency}: "))
        converted = ccs.convert("MDL", to_currency, amount)
        print(f"{amount} MDL is equal to {converted} {to_currency}")
    else:
        to_currency = "MDL"
        amount = float(input(f"Enter amount in {from_currency} to convert to MDL: "))
        converted = ccs.convert(from_currency, "MDL", amount)
        print(f"{amount} {from_currency} is equal to {converted} MDL")
