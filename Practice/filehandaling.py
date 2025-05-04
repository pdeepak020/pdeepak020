exmp2='text.txt'
with open(exmp2, 'w') as writefile:
    writefile.write("This is line A\n")
    writefile.write("This is line B\n")

with open(exmp2,'r') as readfile:
    #print(readfile.read()) # will read all lines
    #print(readfile.readlines()) # will read line in single line ['This is line A\n', 'This is line B\n']
    #print(readfile.read(4)) # will read 4 char of line
    print(readfile.readline()) # will read first line
    print(readfile.readline()) # will read second line
    print(readfile.mode)


# to copy file
#we can aslo use mode rb mode to read only binary
with open('Example2.txt','r') as readfile:
    with open('Example3.txt','w') as writefile:
          for line in readfile:
                writefile.write(line)