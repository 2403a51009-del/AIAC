def convert_temperature(value, from_unit, to_unit):
    # Convert input to Celsius first1
    
    if from_unit == 1:  # Celsius
        celsius = value
    elif from_unit == 2:  # Fahrenheit
        celsius = (value - 32) * 5/9
    elif from_unit == 3:  # Kelvin
        celsius = value - 273.15
    else:
        raise ValueError("Invalid input unit.")

    # Convert from Celsius to target unit
    if to_unit == 1:  # Celsius
        result = celsius
        unit_str = "Celsius"
    elif to_unit == 2:  # Fahrenheit
        result = celsius * 9/5 + 32
        unit_str = "Fahrenheit"
    elif to_unit == 3:  # Kelvin
        result = celsius + 273.15
        unit_str = "Kelvin"
    else:
        raise ValueError("Invalid output unit.")

    return result, unit_str

def temperature_converter():
    while True:
        print("Temperature Converter")
        print("Choose the input unit:")
        print("1. Celsius")
        print("2. Fahrenheit")
        print("3. Kelvin")
        try:
            from_unit = int(input("Enter the number corresponding to the input unit: "))
            if from_unit not in [1, 2, 3]:
                print("Invalid input unit. Please try again.\n")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.\n")
            continue

        try:
            value = float(input("Enter the temperature value: "))
        except ValueError:
            print("Invalid temperature value. Please enter a number.\n")
            continue

        print("Choose the output unit:")
        print("1. Celsius")
        print("2. Fahrenheit")
        print("3. Kelvin")
        try:
            to_unit = int(input("Enter the number corresponding to the output unit: "))
            if to_unit not in [1, 2, 3]:
                print("Invalid output unit. Please try again.\n")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.\n")
            continue

        result, unit_str = convert_temperature(value, from_unit, to_unit)
        print(f"Converted temperature: {result:.2f} {unit_str}\n")

        again = input("Do you want to convert another temperature? (y/n): ").strip().lower()
        if again != 'y':
            print("Exiting Temperature Converter.")
            break

if __name__ == "__main__":
    temperature_converter()
