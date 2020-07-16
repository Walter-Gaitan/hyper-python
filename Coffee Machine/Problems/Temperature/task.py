def fahrenheit_to_celsius(temps_f):
    temps_c = (int(temps_f) - 32) * 5 / 9
    return round(temps_c, 2)


def celsius_to_fahrenheit(temps_c):
    temps_f = int(temps_c) * 9 / 5 + 32
    return round(temps_f, 2)


def main():
    """Entry point of the program."""
    temperature, unit = input().split()  # read the input
    if unit == 'F':
        return print(fahrenheit_to_celsius(temperature), 'C')
    else:
        return print(celsius_to_fahrenheit(temperature), 'F')
