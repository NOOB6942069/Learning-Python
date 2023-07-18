#Type casting = convert the data type of a value to another data type.
#now lets do some examples 
x = 1 #intr
y = 1.1 #float
z = '1' #str
#now lets just print these 
print(x)
print(y)
print(z)
#nice works perfectly fine.
#now lets try to change the data type with the methods that we did in the variable chapter
#lets change the data type of z from an str to a int 
print(int(z)) #now doing this the print command will print the str as an intr
print(int(y))#now lets make y a float an int 
print(float(x)) # lets try to make an int to a float is it even possible ?
#nicely done but these changes are not permanent and only works in the specific print command
# lets make the changes permanent 
z = int(z) # lets permanently change the value of z to be an int
y = str(y)#changing the value of y to be a str 
x = float(x) #changing the vlaue of x to a float from an int 
#lets prints these now in one line of code. 
print(z, y, x )
#successfully done.
#now after type casting we can use a strg to do math becuase the value now behaves like an int 
#lets try it 
print(z+ 5) # the answer should be 6 
#boom now we can use a str as an int 
#chapter ends here.