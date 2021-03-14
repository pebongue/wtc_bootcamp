#method to convert hour(s) to second(s)
def hour_to_second(hour):
    return hour*60*60

#ask the user for the hour(s)
print('This code request an hour value from the user, converts it in second and return the value.')
hour = int(input("Input hour value :"))

#check to ensure no negative hours' value
while hour < 0:
    hour = int(input("Input 'a positive' hour value :"))

#display the converted value to second - this is where you test the hour_to_second method
print(f"The total seconds equivalent is {hour_to_second(hour)} second(s)")