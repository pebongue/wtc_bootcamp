#method to compare 2 numbers and return the largest
def largest_value(a, b):
    return max(a,b)

print('This short code will determine the largest value between 2 numbers.')

#Ask users for input values - no need to worry about the parity
a = float(input("Input the 1st number :"))
b = float(input("Input the 2nd number :"))

#test the largest_value method here
print("The largest value between {} and {} is {}".format(a,b,largest_value(a,b)))