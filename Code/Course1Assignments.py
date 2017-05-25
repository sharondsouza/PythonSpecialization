from click._compat import raw_input

#Assignment 1
# the code below almost works
print("hello world")

#Assignment 2.2
name = input("Enter your name")
print("Hello", name)

#Assignment 2.3
hrs = raw_input("Enter Hours:")
rate = raw_input("Enter the rate per hour:")
hrs=float(hrs)
rate=float(rate)
pay=hrs*rate
print(pay)

#Assignment 3.1
hrs=float(input('Enter the number of hours worked:'))
rate=float(input('Enter the rate of pay per hour:'))
if 0<hrs<=40:
    pay=hrs*rate
elif hrs>40:
    rate1=1.5*rate
    hrs1=hrs-40
    pay=(hrs1*rate1)+(40*rate)
else:
    print('Invalid number of hours entered.')
print(pay)

#Assignment 3.2
score=float(input('Enter your score:'))
if 0.0<score<0.6:
    grade='F'
elif 0.6<=score<0.7:
    grade='D'
elif 0.7<=score<0.8:
    grade='C'
elif 0.8<=score<0.9:
    grade='B'
elif 0.9<=score<1.0:
    grade='A'
else:
    print('Invalid score.')
    exit()
print(grade)

#Assignment 4.6
def computepay(h,r):
    if 0<h<=40:
        p=h*r
    elif hrs>40:
        r1=1.5*r
        h1=h-40
        p=(h1*r1)+(40*r)
    else:
        print('Invalid number of hours entered.')
    return p

hrs=float(input('Enter the number of hours worked:'))
rate=float(input('Enter the rate of pay per hour:'))

pay=computepay(hrs,rate)
print(pay)

#Assignment 5.2
smallest=None
largest=None
while True:
    user_num=raw_input('Enter a number:')
    try:
        if user_num=='Done':
            break        
        else:
            usrnum=int(user_num)
            if smallest==None or usrnum<smallest:
                smallest=usrnum
            elif largest==None or usrnum>largest:
                largest=usrnum
    except:
        print('Invalid input.')
print('Maximum is',largest)
print('Minimum is',smallest)

 
