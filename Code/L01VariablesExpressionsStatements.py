                                           
print("Hello World!")                       #basic print statements
print("So typical!")

a=6                                         #storing values in a variable
print("result 1 is")
print(a)

a=a+5                                       #operators and operands
print("result 2 is")
print(a)
                
complete_quotient=7/3                       #modulus and division
quotient=7//3
remainder=7%3
print("complete quotient is")
print(complete_quotient)
print ("quotient is")
print(quotient)
print("remainder is")
print(remainder)

data=input("What day is it today? \n")      #taking user input and eliminating type errors
str(data)
print("It's %s" %data)
date="What is the date today? \n"
today=int(input(date))                      #converting input data type to integer. It is string by default.
print("It's the %d" %today)

print("--------------EXERCISES---------------------- \n")

prompt="what is your name? \n"              #Exercise 2
name=input(prompt)
print ("Hello %s" %name)
                                            
hours=int(input("Enter no. of hours worked"))   #Exercise 3 
rate=int(input("Enter rate of wage"))
your_pay=hours*rate
print ("Your pay would be %d" %your_pay)

width=17                                    #Exercise 4
height=12.0
a= width//2
b=width/2.0
c=height/3
d=1+2 * 5
print (a,b,c,d)

cel_temp=int(input("WHat is the current temperature on the Celcius scale?"))    #Exercise 5
print ("I will now convert it to celcius for you")
far_temp=(cel_temp*1.8)+32
print("The temperature in Farenheit is %d" %far_temp)


