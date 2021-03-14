'''
The program calculate the sum of 2 integers in the range(0,9)
Print an error if the inputs are out of range and terminate
'''

#method to calculate the total a + b if in range
def calculate_sum(a,b):
    if (a in range(0,10)) and (b in range(0,10)):
        ab_total = a + b
        if ab_total in range(15,21):
            return 20
        else:
            return ab_total
    else:
        return -1

#ask user for 2 integers
a = int(input('Input value A: '))
b = int(input('Input value B: '))

#use a condition to end the program if not in range, and print the sum otherwise
if calculate_sum(a,b) == -1:
    print("NotInRangeError: both {} and {} are not in the range [0...9].".format(a,b))
    #break
else:
    print("The sum value is {}".format(calculate_sum(a,b)))