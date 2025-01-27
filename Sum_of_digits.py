digit=int(input("Enter a number:"))
sum=0
while digit>0:
    reminder=digit%10
    sum+=reminder
    digit=digit//10
print("The sum of the digits is: ",sum)