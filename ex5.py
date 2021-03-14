#ask user for a number
number = float(input('Input a number: '))

if number > 0:
    print('Your number is positive.')
elif number < 0:
    print('Your number is negative.')
else:
    print('Your number is zero.')