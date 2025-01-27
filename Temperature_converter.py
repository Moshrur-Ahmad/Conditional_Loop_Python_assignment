temperature=float(input("Enter the temperature in celcius: "))
fahrenheit=(temperature*9/5)+32
kelvin=temperature+273.15
if(temperature>0):
    print("The temperature in Fahrenheit is: ",fahrenheit)
elif(temperature<0):
    print("The temperature in Kelvin is: ",kelvin)