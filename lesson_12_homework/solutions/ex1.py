def convert_temperature(temperature, unit):
    if unit == "C":
        converted_temperature = (temperature * 9 / 5) + 32
        converted_unit = "F"
    elif unit == "F":
        converted_temperature = (temperature - 32) * 5 / 9
        converted_unit = "C"
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
        return

    return converted_temperature, converted_unit


temperature = float(input("Enter the temperature: "))
unit = input("Enter the current unit (C/F): ")

converted_temperature, converted_unit = convert_temperature(temperature, unit.upper())
print(f"Converted temperature: {converted_temperature} {converted_unit}")
