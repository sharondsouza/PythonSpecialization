#NOTE: COMMENT OUT EVERY OTHER FOR LOOP WHEN EXECUTING ANY ONE FOR LOOP. THE CONTINUE LINES WILL INHIBIT LINE BY LINE EXECUTION


from click._compat import raw_input
"""
filename=raw_input("Enter the name of the file you want to open:")          #allows user to choose the file
try:
    file=open(filename)                           #open a file
except:
    print("This file cannot be opened. Please try again with the correct filename.")
    exit()          #required otherwise it gives a traceback due to calling 'file' in line 10
count=0                         
for line in file:                                   #count number of lines in a file
    count=count+1
    if line.startswith('a') or line.startswith('r'):
        line=line.rstrip()
        print(line)                                 #gives extra whitespaces and new lines. Use rstrip to get rid of this.
print("Total number of lines in the file:",count)

print("--------------------------------")

#alternative instead of the one on top
for line in file:
    if not line.startswith('s'):
        continue
    else:
        print(line)
        
#another one
for line in file:                                   #gives lines containing 'are'
    if line.find('are')==-1:
        continue
    print(line)
"""

inp=raw_input("Enter the name of the file you want to create:")
writing_to_file=open(inp, 'w')
someline=" \n This is going to be some additional line that you will not want here."
writing_to_file.write(someline)
writing_to_file.close()
print('All done!')


print('\n------------------------EXERCISES------------\n')

filename=raw_input('Enter the name of the file you want to open:')
try:
    contents=open(filename)
except:
    print('This file cannot be opened. Kindly check the filename and try again.')
    exit()
for line in contents:
    finaline=line.rstrip()          #removes the redundant new line
    print(finaline.upper())         #puts everything in upper case 

total=0
count=0
filename=raw_input('Enter the name of the file you want to open:')
try:
    contents=open(filename)
except:
    print('This file cannot be opened. Kindly check the filename and try again.')
    exit()
for line in contents:
    if line.startswith('X-DSPAM-Confidence'):
        print(line)
        spacon=float(line[19:])
        print(spacon)
        total=total+spacon
        count=count+1

print('The total value is:',total)
print('The total number of values is:',count)
avg=total/count
print('The average of the values is:',avg)