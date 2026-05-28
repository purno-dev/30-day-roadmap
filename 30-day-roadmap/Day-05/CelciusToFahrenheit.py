celcius = float(input("Enter Celcius Value:"))
def celciusToFahrenheit (x):
    return (9/5*celcius)+32
print(f"{celcius:.2f}° Celcius is {celciusToFahrenheit(celcius):.2f}° Fahrenheit")