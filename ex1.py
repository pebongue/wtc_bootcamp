import datetime

#method to calculate the year someone turns 100 given their age
def your_centenary(age):
    current_year = datetime.datetime.now().year
    return current_year + (100 - age)

#Ask user for their name and age
name = input("what is your name? :")
age = abs(int(input("How old are you? :")))

#personal message for when the user turns 100
print("Hello "+name+ "! You will turn 100 in {}.".format(your_centenary(age)))