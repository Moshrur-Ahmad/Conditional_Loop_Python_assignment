age=int(input("Enter the age: "))
if(age<=1):
    print("Infant")
elif(age>1 and age<=3):
    print("Toddler")
elif(4<=age<=12):
        print("Child")
elif(13<=age<=19):
   print("Teenager")
else:
   print("Adult")
    