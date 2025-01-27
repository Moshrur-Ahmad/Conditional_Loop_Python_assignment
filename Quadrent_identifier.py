x=int(input("Enter the x coordinate: "))
y=int(input("Enter the y coordinate: "))
if(x>0 and y>0):
    print("The point lies in the first quadrent")
elif(x<0 and y>0):
    print("The point lies in the second quadrent")
elif(x<0 and y<0):
    print("The point lies in the third quadrent")
elif(x>0 and y<0):
    print("The point lies in the fourth quadrent")
else:
    print("The point lies in the origin")