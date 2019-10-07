for celcius in range(0,301,20):
    fahrenheit = ((9/5) * celcius) + 32
    kelvin = celcius + 273
    print("{}   {}   {}".format(celcius,fahrenheit,kelvin))
