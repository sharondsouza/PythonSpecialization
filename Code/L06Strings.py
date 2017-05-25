#Basics of parsing strings
fruit='jackfruit'
print("The third letter of the word %s is %s" %(fruit, fruit[2]))
print("The last letter of the word %s is %s" %(fruit, fruit[-1]))
long=len(fruit)
print("The second-last letter of the word %s is %s" %(fruit, fruit[long-2]))

#printing each letter of the word
index=0
print("The letters printed are -")
while index<long:
    alpha=fruit[index]
    print(alpha)
    index=index+1

print("-------------------------------")

#printing letters of the same word backwards - Exercise 1
index=long-1
print("The letters printed backward are -")
while 0<=index<long:
    alpha=fruit[index]
    print(alpha)
    index=index-1
    
print("---------------------------")

#how to do the same thing with a for loop
print("Printing all the letters again - ")
for fr in fruit:
    print(fr)
    
#slicing a string
print("---------------------------")
print(fruit[0:2])
print(fruit[4:8])
print(fruit[5:9])
print(fruit[3:])
print(fruit[:3])
print(fruit[2:2])
print(fruit[:])

print("----------------------------")

#counting number of occurrences of a particular letter in a string i.e. a COUNTER
statement="she sells sea shells on the sea shore."
count=0
for letter in statement:
    if letter=='s':
        count=count+1
print("The letter s is present %d times in the statement - %s" %(count,statement))


#defining a function to perform the counting task
def count(let,state):
    cntr=0
    for char in state:
        if char==let:
            cntr=cntr+1
    return cntr

repsofL=count('l',statement)
print("The letter L is repeated %d number of times in the statement - %s" %(repsofL,statement))


print("------------------------------")

#utilization of the IN operator & concatenation
verdict='a' in statement
print("Output of an 'in' statement is ", verdict)
word=input("Enter the word you want to compare:")
if word<'apples':
    print('Your word ' +word+ ' comes before apples.')
elif word>'apples':
    print('Your word ' +word+ ' comes after apples.')
elif word=='apples':
    print('Your word is apples itself.')
else:
    print("Don't compare. Just move on.")
    
print("------------------------------")

#using string methods
print("Some output of string methods utilized on the example statement can be seen below:")
print("\n Capitalized:",statement.capitalize())
print("\n Casefolded:",statement.casefold())
print("\n No. of times the letter s occurred:",statement.count('s'))
print("\n The position of the first occurrence of the letter a:",statement.find('a'))          #gives the position and not the occurence of the letter
print("\n Putting the whole statement in upper case:",statement.upper())
print("\n Usage of startswith:",statement.startswith('lala'))
print("\n Another example of the above:",statement.startswith('s'))
print("\n Replacing all the s with S:",statement.replace('s','S'))

print("------------------------------")

#parsing more complicated strings. This example extracts the email ID from the said string
frommail="From: Dsouza, Sharon (GE Transportation) [mailto:sharon.dsouza@ge.com]"
start=frommail.find(':',10)
end=frommail.find(']')
print("String Parsing Example Output -")
print("The email ID you are looking for is:",frommail[start+1:end])

print("------------------------------")

print("-----------EXERCISES---------")
string="X-DSPAM-Confidence:0.8475"
initial=string.find(':')
capture=string[initial+1:]
cap_actual=float(capture)
print("The float converted number is %g" %cap_actual)