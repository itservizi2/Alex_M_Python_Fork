temp = float(input("Enter the temperature: "))
unit = input("Enter the current unit (C/F): ")


def convert_temperature(temperature, unit):
    if unit.upper() == "C":
        return (temperature * 9 / 5) + 32
    elif unit.upper() == "F":
        return (temperature - 32) * 5 / 9


converted_temp = convert_temperature(temp, unit)

if unit.upper() == "C":
    print(f"Converted temperature: {converted_temp} F")
elif unit.upper() == "F":
    print(f"Converted temperature: {converted_temp} C")
