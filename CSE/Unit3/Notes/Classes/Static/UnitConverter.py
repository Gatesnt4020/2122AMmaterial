class UnitConverter:

#static method, you don't need self
    @staticmethod   #@symbol is a decorator 
    def celsiusToFahrenheit(c):
        fah = c*9/5+32
        return fah

    #fahrenheitToCelsius(f)
    @staticmethod
    def fahrenheitToCelsius(f):
        cel = (f-32)*5/9
        return cel

    #c to k
    @staticmethod
    def celsiusToKelvin(c):
        k = c+273.15
        return k

    #f to k 
    @staticmethod
    def fahrenheitToKelvin(f):
        c =UnitConverer.fahrenheitToCelsius(f)
        k =UnitConverer.celsiusToKelvin(c)
        return k

    #k to c
    @staticmethod
    def kelvinToCelsius(k):
        c = k-273.15
        return c

    #k to f 
    @staticmethod
    def kelvinToFahrenheit(k): 
        c =UnitConverer.kelvinToCelsius(k)
        f=UnitConverer.celsiusToFahrenheit(c)
        return f
