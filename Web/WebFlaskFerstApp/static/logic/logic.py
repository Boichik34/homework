def convert_to_fahrenheit(value):
    temperature = 9 / 5 * float(value) + 32
    return temperature


def convert_to_kelvin(value):
    temperature = float(value) + 273.15
    return temperature


def calculate_bmi(weight, height):
    bmi = float(weight) / ((float(height) / 100) ** 2)
    return bmi