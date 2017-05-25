from click._compat import raw_input
import string
eng2fr=dict()
print(eng2fr)

eng2fr['one']='un'
eng2fr['two']='deux'
print(eng2fr)
print(eng2fr['two'])
print(len(eng2fr))

print('one' in eng2fr)
print('un' in eng2fr)
val=list(eng2fr.values())
print(val)
print('un' in val)


print('---------------------------------------------------------')


#counting the occurrences of letters in a word
mychoice='nfkjernthutoijdlansdvkeorjuefniervjdfjvzczsndkwoewjrcdnmfhbgerkuhweoirjqeo'
counts=dict()
for letter in mychoice:
    if letter not in counts:
        counts[letter]=1
    else:
        counts[letter]=counts[letter]+1
print(counts)

#counting using the get method
counts2=dict()
for letter in mychoice:
    counts2[letter]=counts2.get(letter,0)+1
print(counts2)


print('---------------------------------------------------------')

filename=raw_input('Enter the name of the file:')
try:
    contents=open(filename)
except:
    print ('This file cannot be opened. Kindly enter the correct file name and try again.')
    exit()
counts3=dict()
for line in contents:
    words=line.split()
    for word in words:
        if word not in counts3:
            counts3[word]=1
        else:
            counts3[word]+=1
print('The dictionary of words is as follows:',counts3)
print("Another way of printing the dictionary is:")
for key in counts3:
    print(key, counts3[key])
#to print only specific values of the dictionary
print('The below words have been repeated:')
for key in counts3:
    if counts3[key]>1:
        print(key,counts3[key])

print('---------------------------------------------------------')

#to print all the entries in alphabetical order
listing=list(counts3.keys())
listing.sort()
print('The dictionary in alphabetical order is as follows:')
for key in listing:
    print(key, counts3[key])
    
print('---------------------------------------------------------')    
    
#with punctuation
counts4=dict()
punctcont=open('romeo-full.txt')
for line in punctcont:
    line=line.translate(line.maketrans('','',string.punctuation))
    line=line.lower()
    words=line.split()
    for word in words:
        if word not in counts4:
            counts4[word]=1
        else:
            counts4[word]+=1
print('The complete list is:', counts4)
listing2=list(counts4.keys())
listing2.sort()
print('In alphabetical order, the list is:')
for each in listing2:
    print(each,counts4[each])