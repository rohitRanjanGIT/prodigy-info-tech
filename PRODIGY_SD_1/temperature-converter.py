def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5.0/9.0
    return celsius

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9.0/5.0) + 32
    return fahrenheit

temperature_format = str(input("Select the conversion you want to perform:\n'F': for Fahrenheit to Celsius.\n'C': for Celsius to Fahrenheit.\nInput: ")).upper()

temperature_given = float(input(f"Enter the provided temperature in {temperature_format}: "))

resultant_temperature = 0

if temperature_format == 'C':
    resultant_temperature = celsius_to_fahrenheit(temperature_given)
    print(f"{temperature_given} Celsius is {resultant_temperature:.2f} Fahrenheit")
elif temperature_format == 'F':
    resultant_temperature = fahrenheit_to_celsius(temperature_given)
    print(f"{temperature_given} Fahrenheit is {resultant_temperature:.2f} Celsius")
else:
    print("Invalid input! Please enter 'F' for Fahrenheit to Celsius or 'C' for Celsius to Fahrenheit.")
