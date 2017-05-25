from click._compat import raw_input
newlist=list()
filename=raw_input('Enter the name of the file you want to open:')
try:
    contents=open(filename)
except:
    print("This file cannot be opened. Kindly verify the name of the file and try again.")
    exit()
for line in contents:
    #line=line.rstrip()
    words=line.split()
    print(words)
    newlist=newlist+words
print('The final list of words is:', newlist)
howmany=len(newlist)
print('The no. of words is ',howmany)
#i=0
final_list=list()
#while 0<=i<howmany:
for word in newlist:
    if word in final_list:
        continue
    elif final_list==None:
        final_list.append(word)
    else:
        final_list.append(word)
        #i=i+1            
howmany2=len(final_list)
print('The final list of words without repetitions is:',final_list)
print('The no. of words now is ', howmany2)

final_list.sort()
print('Arranged alphabetically, this is what we get:',final_list)


    
print('----------------------')

mailfile=raw_input('Enter the name of the mail file you want to inspect:')
try:
    mailcont=open(mailfile)
except:
    print('This file cannot be opened. Please enter a valid filename and try again.')
    exit()
count=0
for line in mailcont:
    line=line.rstrip()
    if line.startswith('From '):
        words=line.split()
        print(words[1])
        count=count+1
print('Total number of lines starting with From:', count)



print('----------------------')

listofnums=list()
i=0
while i>=0:
    usernum=input('Enter the number you want to add to the list:')
    try:
        if usernum=='Done':
            break
        else:
            usernum=int(usernum)
            listofnums.append(usernum)
    except:
        print('Kindly enter only numbers. Try again.')
        exit()

print('Your list is: ',listofnums)
print('Total number of entries is ',len(listofnums))
print('The maximum of the numbers entered is:', max(listofnums))
print('The minimum of the numbers entered is:', min(listofnums))