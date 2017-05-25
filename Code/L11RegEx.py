import re
from click._compat import raw_input
file=open('mbox-short.txt')
#for line in file:
#    line=line.strip()
 
#BASIC SEARCH METHODS   
#    if re.search('From:',line):
#    if re.search('From:.+@',line):
#    if re.search('From:...',line):
#        print(line)
#print("-----------------------------------")     
    
#USING FINDALL AND THE S    
#    x = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]',line)       #all lines with the string in it
#    if len(x)>0:
#        print(x)
    
#print("-----------------------------------") 

#seaching all the spam confidence lines
#    if re.search('^X\S*: [0-9.]+',line):
#        print(line)
        
#searching and printing only the floating point values. Emphasis on the common brackets in the expression
#    y = re.findall('^X-\S*: ([0-9].+)',line)
#    if len(y)>0:
#        print(y)

#Finding the 'hour' values from the test file
#    z=re.findall('^From .* ([0-9][0-9]):.*',line)
#    if len(z)>0:
#        print(z)

#Example without \S
#x = 'From: Using the : character'
#y = re.findall('^F.+:', x)
#print (y)

'''
#EXERCISE 1
filename='mbox.txt'
file1=open(filename)
regexp=raw_input('Enter a regular expression:')
inp= (''+regexp+'.*')
print(inp)
count=0
for line in file1:
    line=line.strip()
    z = re.findall(''+inp+'',line)
    if len(z)>0:
        count=count+1
        print(z)
print('%s had %d lines that matched %s' %(filename,count,regexp))


#EXERCISE 2
filename='mbox.txt'
file2=open(filename)
count1=0
sum1=0
for line in file2:
    ext=re.findall('New Revision: (.*)',line)
    if len(ext)>0:
        ext[0]=int(ext[0])
        sum1=sum1+ext[0]
        count1=count1+1
avgofnums=sum1/count1
avground=round(avgofnums,7)
print(avground)
'''

thefile=raw_input("Enter the filename:")
cnts=open(thefile)
totalof=0
counter=0
for line in cnts:
    words=line.split()
    for word in words:
        isnum=re.findall('([0-9]+)',word)
        if len(isnum)>0:
            isnum=int(isnum[0])
            totalof=totalof+isnum
            counter=counter+1
print(totalof)
print(counter)