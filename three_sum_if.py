"""
This method calculate the sum of 3 integers

if 2 of the given numbers are equal, the sum returned is 0(zero)
"""
def three_sum(a,b,c):
    if (a == b) or (a == c) or (b == c):
        return 0
    else:
        return a + b + c

#request 3 integers from the user
print('This code request 3 values a, b and c from the user and calculate the sum.')
a = int(input("Input 1st integer :"))
b = int(input("Input 2nd integer :"))
c = int(input("Input 3rd integer :"))

#display the sum if
print('The sum of the 3 numbers is ' + str(three_sum(a,b,c))) 