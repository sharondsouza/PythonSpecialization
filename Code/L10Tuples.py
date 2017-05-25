#basics of tuples
import string
from click._compat import raw_input
tuple1=('q','w','e','r','t','y')
tuple2=('a',)
tuple3=tuple()
tuple4=tuple('happiness')
print(tuple4)
print(tuple1[3])
print(tuple4[1:4])
tuple5=tuple1+tuple2
print(tuple5)

res1=(0,1,2545)<(0,2,3)
print(res1)

#reverse sorting using tuples
sente='but soft what light in yonder window breaks'
words=sente.split()
senlist=list()
for word in words:
    senlist.append((len(word),word))
print(senlist)
senlist.sort(reverse=True)
print(senlist)

senlist2=list()
for length,word in senlist:
    senlist2.append(word)
print(senlist2)


#multiple assignments using tuples
a=['happy','sad','creepy']
x,y,z=a
print(a)
print(x)
print(y)
print(z)

addr='whackadoodle@gmail.com'
username,domain=addr.split('@')
print(username)
print(domain)

#dictionaries and tuples
lista=list()
dicta1={'a':10,'b':5,'c':15,'d':7}
tup1=list(dicta1.items())
print(tup1)
tup1.sort()
print(tup1)
for key,val in tup1:
    lista.append((val, key))
lista.sort()
print(lista)

#finding the most common words in a text
poetry=list()
poetrydict=dict()
opener=raw_input('Enter the name of the file you want to open:')
content=open(opener)
for line in content:
    line=line.translate(str.maketrans('','',string.punctuation))
    line=line.lower()
    words=line.split()
    for word in words:
        poetry.append(word)
print(poetry)
for each in poetry:
    if each not in poetrydict:
        poetrydict[each]=1
    else:
        poetrydict[each]+=1
print(poetrydict)
poetuple=list(poetrydict.items())
print(poetuple)
poetrylist=list()
for word,rep in poetuple:
    poetrylist.append((rep,word))
print(poetrylist)
poetrylist.sort(reverse=True)
print(poetrylist)
for rep,which in poetrylist[0:10]:
    print(which, rep)
