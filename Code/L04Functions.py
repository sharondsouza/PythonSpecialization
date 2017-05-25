import random               	#importing built-in functions
import math

a=max("happiness")              #using min and max ---> built-in functions
print("%s \n" %a)
b=min("happiness")
print("%s \n" %b)

c=int(len("She sells sea shells on the sea shore."))    #find the length of a string
print("length = %d \n" %c)

d=int(39.9999)                  #data type conversions using built-in functions
print("%d \n" %d)
e=str(39.99999)
print("%s \n" %e)
f=float(39)
print("%f \n" %f)

for i in range(15):             #generate x no. of random numbers between 0.0 and 1.0
    x=random.random()
    print(x)
    
print("\n \n")
    
for i in range(12):             #generate x no. of random integers from 4 to 400
    x=random.randint(4,400)
    print(x)
    
print("\n \n")

g=math.sqrt(3)/2                #example of a math function usage
print("%s \n" %g)


def when_i_call():              #defining and calling your own function
    print("You called the function.\n")
    
print("----------- \n")

def twice_only():
    when_i_call()
    when_i_call()
    
twice_only()                    #only this gets printed


def apples(test):               #using parameters in a function
    print(test)
    a=test+'fruit'
    print(a)
apples('orange')
print("\n")
apples('mango')

def mult(x,y,z):                #using multiple parameters in a function
    value=x*y*z
    return value

j=mult(3,4,5)
exam=int(j)
print("The result will be printed twice. Here %d and here %d." %(exam,exam))


print("--------------EXERCISES---------------------- \n")

def computepay_under40(a,b):                #Exercise 6
    value=a*b
    return value
def computepay_over40(a,b):
    value=a*b*1.5
    return value
hr=input("Enter no. of hours worked")   
rt=input("Enter rate of wage")
try:
    hours=int(hr)    
    rate=int(rt)
    if 0<hours<=40 :
        pay_under40=computepay_under40(hours, rate)
        your_pay=int(pay_under40)
        print ("Your pay is %d" %your_pay)
    elif hours>40:
        pay_over40=computepay_over40(hours, rate)
        your_pay=int(pay_over40)
        print ("Your pay is %d" %your_pay)
    else:
        print ("No pay.")
except:
    print("\n Enter integers only, please.") 
    
    
scr=input("Enter your score to obtain your grade.")             #Exercise 7
def computegrade(value):
    if 0.0<value<1.0:
        if 0.9<=value<1.0:
            print("Your grade = A")
        elif 0.8<=value<0.9:
            print("Your grade = B")
        elif 0.7<=value<0.8:
            print("Your grade = C")
        elif 0.6<=value<0.7:
            print("Your grade = D")
        else:
            print("Your grade = F")
    else:
        print ("Invalid score. Unable to generate grade.")

try:
    score=float(scr)
    computegrade(score)
except:
    print("Kindly enter your numeric score between 0.0 and 1.0")