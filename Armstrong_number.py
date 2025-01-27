num=int(input("Enter a number: "))
original_num=num
sum=0
while(num>0):
    digit=num%10
    sum+=(digit)**3
    num//=10
if(sum==original_num):
    print("The number is an Armstrong number")
else:
    print("The number is not an Armstrong number")