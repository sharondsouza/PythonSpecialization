from click._compat import raw_input
'''
dictofmail=dict()
file=raw_input('Enter file name:')
contents=open(file)
for line in contents:
    if line.startswith('From '):
        words=line.split()
        check=words[1]
        if dictofmail==None or check not in dictofmail:
            dictofmail[check]=1
        else:
            dictofmail[check]+=1
#print(dictofmail)
t1=list(dictofmail.items())
t2=list()
print(t1)
for mail,cnt in t1:
    t2.append((cnt,mail))
print(t2)     
largest=0
largemail=None
for cnt,mail in t2:
    if cnt>largest:
        largest=cnt
        largemail=mail
print(largemail,largest)

t2.sort(reverse=True)
print(t2)    
'''
hrs_l=list()
hrs_d=dict()
flname=raw_input('Enter file name:')
cont=open(flname)
for each in cont:
    if each.startswith('From '):
        posi=each.find(':')
        hr=each[posi-2:posi]
        if hrs_d==None or hr not in hrs_d:
            hrs_d[hr]=1
        else:
            hrs_d[hr]+=1
hrs_l=list(hrs_d.items())
hrs_l.sort()
for hr,count in hrs_l:
    print(hr,count)
        

        