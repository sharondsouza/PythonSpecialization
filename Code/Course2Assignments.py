
#Assignment 6.5
text = "X-DSPAM-Confidence:    0.8475";
pos=text.find('.')
slice1=text[pos-1:pos+5]
print(float(slice1))


#Assignment 7.1
from click._compat import raw_input
file=raw_input('Enter file name:')
contents=open(file)
for line in contents:
    print(line.upper())
  
#Assignment 7.2
#from click._compat import raw_input
count=0
added=0
file=raw_input('Enter file name:')
contents=open(file)
for line in contents:
    if line.startswith('X-DSPAM-Confidence:'):
        pos= line.find('.')
        numb=float(line[pos-1:pos+5])
        count=count+1
        added=added+numb
    else:
        continue
avg=added/count
print('Average spam confidence:',avg)

#Assignment 8.4
#from click._compat import raw_input
la=list()
file=raw_input('Enter file name:')
contents=open(file)
for line in contents:
    words=line.split()
    for word in words:
        if la==None or word not in la:
            la.append(word)
        else:
            continue
la.sort()
print(la)


#Assignment 8.5
count=0
#from click._compat import raw_input
file=raw_input('Enter file name:')
contents=open(file)
for line in contents:
    if line.startswith('From '):
        words=line.split()
        count=count+1
        print(words[1])
print ('There were %d lines in the file with From as the first word' %count)


#Assignment 9.4
dicta=dict()
#from click._compat import raw_input
file=raw_input('Enter file name:')
contents=open(file)
for line in contents:
    if line.startswith('From '):
        words=line.split()
        key=words[1]
        if key not in dicta:
            dicta[key]=1
        else:
            dicta[key]=dicta[key]+1
largest=0
for val in dicta:
    comp=dicta[val]
    if comp>largest:
        val1=val
        largest=comp
print(val1,largest)
