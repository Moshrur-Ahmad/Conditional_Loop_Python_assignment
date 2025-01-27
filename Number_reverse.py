num=int(input("Enter a number: "))
rnum=0
while(num>0):
    ldigit=num%10
    rnum=(rnum*10)+ldigit
    num=num//10
print("The revese of the number is: ",rnum)