from builtins import float
x=1                                                         #conditional execution
if x > 0 :
    print("This works!")
x=-2
if x > 0 :
    print("It's greater than zero.")
elif x == 0:
    print("It's equal to zero")
else:
    print("It's less than zero.")
    
x=3                                                         #nested conditionals
y=10
if x>y:
    print("Apples.")
else:
    if x==y:
        print("Oranges.")
    elif x<y:
        print("Bananas.")
    else:
        print("Mangoes.")
        
if x>0 and x<10:                                            #logical operators
    print("x is less than 10 and greater than 0")
        

cel=input("What is the current temperature on the Celcius scale?")    #Using try and except to get rid of datatype errors
try:
    cel_temp=int(cel)
    print ("I will now convert it to celcius for you")
    far_temp=(cel_temp*1.8)+32
    print("The temperature in Farenheit is %d" %far_temp)
except:
    print("What did you just type?!")
    
    
x=1                                                         #The Guardian Pattern
y=0
if x>=2 and (x/y)>2:
    print ("Something must be wrong here")
else:
    print ("The first condition is false")
x=2
y=0

#UNCOMMENT THESE LINES ONLY WHEN STUDYING THE GUARDIAN PATTERN. THESE LINES GENERATE AN ERROR. HENCE.

#if x>=2 and (x/y)>2:
#   print ("The second condition is false. Before printing this you will encounter an error.")

print("--------------EXERCISES---------------------- \n")    
    
hr=input("Enter no. of hours worked")   #Exercise 1 & 2
rt=input("Enter rate of wage")
try:
    hours=int(hr)    
    rate=int(rt)
    if 0<hours<=40 :
        your_pay=hours*rate
        print ("Your pay is %d" %your_pay)
    elif hours>40:
        your_pay=hours*rate*1.5
        print ("Your pay is %d" %your_pay)
    else:
        print ("No pay.")
except:
    print("\n Enter integers only, please.")    
    
    
scr=input("Enter your score to obtain your grade.")             #Exercise 3
try:
    score=float(scr)
    if 0.0<score<1.0:
        if 0.9<=score<1.0:
            print("Your grade = A")
        elif 0.8<=score<0.9:
            print("Your grade = B")
        elif 0.7<=score<0.8:
            print("Your grade = C")
        elif 0.6<=score<0.7:
            print("Your grade = D")
        else:
            print("Your grade = F")
    else:
        print ("Invalid score. Unable to generate grade.")
except:
    print("Kindly enter your numeric score between 0.0 and 1.0")