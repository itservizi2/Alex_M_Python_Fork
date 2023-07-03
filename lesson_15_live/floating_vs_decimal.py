from decimal import Decimal

from _decimal import ROUND_HALF_UP, ROUND_HALF_DOWN

decimal_value = Decimal('1.32')
print(decimal_value)

print(decimal_value * 2)
print(decimal_value ** 2)
print(decimal_value / 2)
print(decimal_value // 2)

float_value = 1.32
print(float_value)

print(float_value * 2)
print(float_value ** 2)
print(float_value / 2)
print(float_value // 2)

print(decimal_value ** 2 == float_value ** 2)

times_2_decimal = decimal_value * 2
times_2_float = float_value * 2
print(times_2_float, times_2_float)
print(Decimal(str(float_value * 2)))
print(Decimal(float_value * 2) == decimal_value * 2)

str_value = '1.32'
float_value = 1.32
decimal_from_str = Decimal(str_value)
decimal_from_float = Decimal(float_value)
decimal_from_float = Decimal(str(float_value))
print(decimal_from_str, decimal_from_float)

print(Decimal('1') == 1.0)

decimal_from_float = Decimal(float_value)
print(decimal_from_float)
print(float(decimal_from_float))

print(Decimal(1.32 - 1.32))

my_demial_value = Decimal('1.12623123123')
new_value = my_demial_value.quantize(Decimal('1.11111'), rounding=ROUND_HALF_UP)
print(my_demial_value)
print(new_value)
