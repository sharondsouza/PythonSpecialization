from click._compat import raw_input

first=[12,13,15,14,32]
second=[33,43,22,5,31]

def removing(themthings):
    del themthings[0]
    return(themthings)

def adding(themthings,val):
    themthings.append(val)
    return(themthings)
print ('The lists are:',first, second)

inp=raw_input('Enter what you want to add to the list:')
print('By adding your selected value to the list, this is what it looks like:',adding(second,inp))
print('By deleting the first item on your selected list, this is what happens:',removing(first))


my_creation=list()
i=0
while i>=0:
    shesay=input("Enter the value you want to add to the list:")
    if shesay=='Done':
        break
    else:
        shesays=int(shesay)
        my_creation.append(shesays)
        i=i+1
print('The contents of the list you built are:',my_creation)

def chop(listname):
    del listname[0]
    del listname[-1]
    return listname

def middle(listname):
    howmany=len(listname)
    del listname[howmany-1]
    listname=listname[1:]
    return listname
   
#funct1=chop(my_creation)
#print('Output of the CHOP function:', funct1)
funct2=middle(my_creation)
print('Output of the MIDDLE function:', funct2)
