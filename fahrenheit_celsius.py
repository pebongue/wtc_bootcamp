#method to convert fahrenheit to celsius and return the value
def fahren_celsius(fahr):
    return (fahr - 32) / 1.8

#ask for the a fahrenheit value from the user
print('This code request an fahrenheit value from the user, converts it to celsius and return the value.')
fahrenheit = float(input("Input fahrenheit value :"))

#test the method here by displaying the conversion
print(f"The celsius equivalent is {int(fahren_celsius(fahrenheit))} degree(s)")