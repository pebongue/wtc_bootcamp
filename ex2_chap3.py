#this function evaluates odd or even number and returns a value
#Hence for simplicity we will only be expecting and using integers
def collatz(number):
    if number%2 == 0:
        number_int_division = number//2
        print("The even number {}//2 = {}".format(number, number_int_division))
        return number_int_division #I am not sure why the exercise said we should return this value
    else:
        number_is_odd = 3*number + 1
        print("The number {} is odd, and 3*({}) + 1 = {}".format(number, number, number_is_odd))
        return number_is_odd

#test the code by simply calling the method since there is a print in it
number = int(input("Enter an integer to evaluate its parity (odd or even) :"))
collatz(number)