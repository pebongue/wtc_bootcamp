print('This short code will calculate the are of a rectangle given positive length and width.')

#Ask users for input values - no need to worry about the parity
length = abs(float(input("Input the length value :")))
width = abs(float(input("Input the width value :")))

#Work out the area of the rectangle by multiply the length by the width
area_rectangle = length*width

print(f'The area of the rectangle with given length = {length}cm and width = {width}cm is Area_Rect = {area_rectangle} square centimeters')