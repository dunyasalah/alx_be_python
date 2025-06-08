CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
KELVIN_OFFSET = 273.15

def celsius_to_fahrenheit(c):
    return c * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def celsius_to_kelvin(c):
    return c + KELVIN_OFFSET

def kelvin_to_celsius(k):
    return k - KELVIN_OFFSET

def main():
    while True:
        print("\nTemperature Conversion Tool")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Celsius to Kelvin")
        print("4. Kelvin to Celsius")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice. Please enter a number.")
            continue

        try:
            if choice == 1:
                c = float(input("Enter temperature in Celsius: "))
                print(f"{c}°C = {celsius_to_fahrenheit(c):.2f}°F")
            elif choice == 2:
                f = float(input("Enter temperature in Fahrenheit: "))
                print(f"{f}°F = {fahrenheit_to_celsius(f):.2f}°C")
            elif choice == 3:
                c = float(input("Enter temperature in Celsius: "))
                print(f"{c}°C = {celsius_to_kelvin(c):.2f} K")
            elif choice == 4:
                k = float(input("Enter temperature in Kelvin: "))
                print(f"{k} K = {kelvin_to_celsius(k):.2f}°C")
            elif choice == 5:
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

if __name__ == "__main__":
    main()
