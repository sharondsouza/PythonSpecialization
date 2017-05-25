x=5
x=x+1                       #updating the value of a variable
print("the new value of x is %d" %x)

print("----------------------------")

while x>0:                  #example of WHILE usage
    print("\n %d" %x)
    x=x-1
print("\n Completed the loop.")   
      
print("----------------------------")

while True:                 #example of infinite loop - "Stop if THIS happens instead of continue till THIS happens.
    line=input('>')
    if line=='Sharon':
        break
    print(line)
print("Completed the infinite loop.")

print("----------------------------")

while True:                 #Infinite loop other example.
    take=input('>')
    if take[2]=='e':
        continue
    if take=='Sharon':
        break
    print(take)
print("Completed the other use of the infinite loop.")

print("----------------------------")

listofthings=['apples','oranges','bananas','mangoes','kiwis']       #for loop usage
for thing in listofthings:                                          #friend is called the Iteration Variable
    print("I bought ", thing)
print("That's all the fruits I bought.")

print("----------------------------")

count=0                                                             #using for loops to count; works like len()
names=['sharon','evan','stephen','sheila','karen','jovita']
for name in names:
    count=count+1
    print("The name is",name)
print("Total number of people is", count)

print("----------------------------")

total=0                                                             #using loops to add; works like sum()
numbers=[3,2,53,132,54,54,21,65,87]
for num in numbers:
    total=total+num
    print("The number now is",num)
print("Total is", total)

print("----------------------------")

largest= None                                                   #These assignments are important. You do not assign them to zero. That would not be a good practice.    
smallest=None
for num in numbers:                                             #find the largest number
    if largest is None or num>largest:
        largest=num
    print("Working numbers in the loop: %d, %d" %(largest,num))
print("The largest number was found to be:",largest)

print("----------------------------")

for num in numbers:                                             #find the smallest number
    if smallest is None or num<smallest:
        smallest=num
    print("Working numbers in the loop: %d, %d" %(smallest,num))
print("The smallest number was found to be:",smallest)

print("----------------------------")

print("--------------EXERCISES---------------------- \n")       #both questions answered here
count=0
total=0
average=None
mini=None
maxi=None

while True:
    num=input("Enter Your Number:")
    try:
        number=int(num)
        count=count+1
        total=total+number
        if mini is None or number<mini:
            mini=number
        if maxi is None or number>maxi:
            maxi=number
    except:
        if num!='Done':
            print("Kindly enter an integer value.")
    if num=='Done':
        print("Total number of entries is: ", count)
        print("Sum of all number entered is:", total)
        average=total/count
        print("Average of all the numbers entered is:", average)
        print("The maximum value entered is:", maxi)
        print("The minimum value entered is", mini)
        break