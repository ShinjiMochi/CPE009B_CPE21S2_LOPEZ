def main():
    class TemperatureConversion:
        def __init__(self, temp=1.0):
            self.temp = temp
    class CelciusToFahrenheit(TemperatureConversion):
        def conversion(self):
            return (self.temp * 9)/5 + 32
    class CelciusToKelvin(TemperatureConversion):
        def conversion(self):
            return self.temp + 273.15

    ## Added Classes
    class FahrenheitToCelcius(TemperatureConversion):
        def conversion(self):
            return (self.temp - 32) * 5/9
    class KelvinToCelcius(TemperatureConversion):
        def conversion(self):
            return self.temp - 273.15

    tempInCelcius = float(input("Enter temperature in Celcius: "))
    convert = CelciusToKelvin(tempInCelcius)
    print(str(convert.conversion()) + "Kelvin")
    convert = CelciusToFahrenheit(tempInCelcius)
    print(str(convert.conversion()) + "Fahrenheit")

    ## Fahrenheit to Celcius
    tempInFahrenheit = float(input("Enter temperature in Fahrenheit: "))
    convert = FahrenheitToCelcius(tempInFahrenheit)
    print(str(convert.conversion()) + "Celcius")

    ## Kelvin to Celcius ##
    tempInKelvin = float(input("Enter temperature in Kelvin: "))
    convert = KelvinToCelcius(tempInKelvin)
    print(str(convert.conversion()) + "Celcius")

main()