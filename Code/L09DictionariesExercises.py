from click._compat import raw_input
newlist=list()
final=dict()
newlist2=list()
final2=dict()
newlist3=list()
final3=dict()
cont=raw_input('Enter the name of the file you want to open:')
try:
    file=open(cont)
except:
    print('This file cannot be opened. Verify the name of the file and try again.')
    exit()
for line in file:
    line.rstrip()
    if line.startswith('From '):
        words=line.split()
        newlist.append(words[2])
        newlist2.append(words[1])
            
for day in newlist:
    if day not in final:
        final[day]=1
    else:
        final[day]+=1
print(final)

for address in newlist2:
    if address not in final2:
        final2[address]=1
    else:
        final2[address]+=1
print(final2)

largest=0
for each in final2:
    if final2[each]>largest:
        largest=final2[each]
        addr=each
        count=final2[each]
    else:
        continue
print('The address that has sent the most no. of messages is %s with %d messages.' %(addr,count))

print(newlist2)
for one in newlist2:
    one=one.split('@')
    newlist3.append(one[1])
print(newlist3)
for domain in newlist3:
    if domain not in final3:
        final3[domain]=1
    else:
        final3[domain]+=1
print(final3)