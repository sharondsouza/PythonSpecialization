#Basics about lists
from click._compat import raw_input
list1=['apples', 'mangoes', 'oranges']
list2=[0.25,'juice', 324, [10,20,'fruit']]
print('The second item in list 2 is:',list2[1])
print("The fourth item in list 2 is:", list2[3])
list1[2]='extras'
print('Updated contents of List 1 are:',list1)

#checking for presence in a list
if 'mangoes' in list1:
    print('It is there.')
else:
    print('It is not there.')

#printing items in a list one by one
print('\nPrinting the items in List 1:')
for item in list1:
    print(item)
print('\nPrinting items in list 2:') 
for each in range(len(list2)):
    print(list2[each])

#list operations - concatenations, deletion, addition etc.    
a=[1,3,2]
b=[6,5,4]
c=a+b
print('\nThe contents of list C are:',c)
d=a*4
e=b*2
print('\nThe contents of List d are:',d)
print('\nThe contents of List e are:',e)
print(d[2:4])
d[2:4]=['banana', 'shmanana']
print('The updated contents of List d are:',d)
e.append('12')
print('The updated contents of list e are:',e)
e.extend(d)
print('The updated contents of list e are:',e)
c.sort()
print('The updated contents of list c are:',c)

g=e.pop(9)
print(g)
print(e)
del e[9]
print(e)
e.remove(1)
print(e)
del e[0:4]
print(e)

list3=[13,54,232,65,3,7,32,99]
print('\nThe contents of list 3 are:',list3)
print('Sum of items in list 3:',sum(list3))
print('Number of items in list 3:',len(list3))
print('Maximum value in list 3 is:',max(list3))
print('Minimum value in list 3 is:',min(list3))

#Program to compute the average
numbers=list()
while True:
    value_taken=input('Enter the number:')
    if value_taken=='Done':
        break
    else:
        val=int(value_taken)
        numbers.append(val)
print(numbers)
avg=((sum(numbers))/(len(numbers)))
print('The average of all the numbers entered is:', avg)

stt='An apple a day keeps the doctor away'
listing1=stt.split()
print('The statement is broken into a list of strings as:',listing1)
one_word=listing1[1]
listing2=list(one_word)
print('the contents of the second word in the statement are:', listing2)
delimiter=' '
stt2=delimiter.join(listing1)
print('The rejoined statement is:', stt2)

#Printing the day of the week from each line that starts with From
count=0
filename=raw_input('Enter the name of the file you want to open:')
try:
    contents=open(filename)
except:
    print('The file cannot be opened. Kindly enter the correct filename and try again.')
    exit()
for line in contents:
    if line.startswith('From'):
        line=line.rstrip()
        #print(line)
        count=count+1
        words=line.split()
        print(words[1])
        
        
        
#Functions and lists
