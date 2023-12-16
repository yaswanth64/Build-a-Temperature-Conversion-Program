def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def temperature_conversion():
    print("Temperature Conversion Program")

    temperature = float(input("Enter temperature value: "))
    original_unit = input("Enter the original unit of measurement (C, F, or K): ").upper()

    if original_unit == "C":
        print(f"\n{temperature} degrees Celsius is equal to:")
        print(f"{celsius_to_fahrenheit(temperature):.2f} degrees Fahrenheit")
        print(f"{celsius_to_kelvin(temperature):.2f} Kelvin")

    elif original_unit == "F":
        print(f"\n{temperature} degrees Fahrenheit is equal to:")
        print(f"{fahrenheit_to_celsius(temperature):.2f} degrees Celsius")
        print(f"{fahrenheit_to_kelvin(temperature):.2f} Kelvin")

    elif original_unit == "K":
        print(f"\n{temperature} Kelvin is equal to:")
        print(f"{kelvin_to_celsius(temperature):.2f} degrees Celsius")
        print(f"{kelvin_to_fahrenheit(temperature):.2f} degrees Fahrenheit")

    else:
        print("Invalid unit of measurement. Please enter C, F, or K.")

if __name__ == "__main__":
    temperature_conversion()
