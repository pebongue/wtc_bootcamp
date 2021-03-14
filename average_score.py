#method to calculate the aveage of the 3 numbers
def average(a, b, c):
    return (a + b + c)/3

#request 3 numbers from the user
print('This code request 3 values a, b and c from the user and return their average.')
a = float(input("Input 1st value :"))
b = float(input("Input 2nd value :"))
c = float(input("Input 3rd value :"))

#display the average
print('The average of the 3 numbers is ' + str(average(a,b,c))) 