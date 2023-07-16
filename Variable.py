# variable is container of a value and behave as the value that it contains.
#now for example lets use a variable and create a string 
name = 'FREN' #now here the variable is name and it contains the value which is FREN
last_name = "pupo"
full_name = name + " "+ last_name 
#print(full_name) #to check the type of variable use 
#print(type(variable))
#print(type(full_name))
# print(name) #Remember do not use Quotes while printing Variables.
#now lets print this in one comand 
#print("Hello " + full_name)
#now lets try another type of variables 
age = 21
age += 1
#print("Helo "+ full_name + "i am "+ age + " Old")
#not gonna work because we used two different type of variables i;e str and int
#now lets display the int with str we will have to use intr as a str
print("Hello "+ full_name+ " "+ "your age is :" + str(age))
#here we used the str(variable) to use a intr variable as a string variable.
#Now the next Data type is going to be Float, its basically the decimle numbers.
height = 500.5
print(type(height)) #this will show us the type of variable in the output window.
#now lets print this
#print("Your Height is " +" " + height+ " cm") # this will mot work as we will have to define the float as a str
print("Your height is :"+ ""+ str(height)+ "Cm")
#boolean = true or false 
money = False
btc = True 
print(type(money))
print("you dont like btc : "+ str(money))
print ("you dont like Fiat: "+str(btc) )
#chapter ends here.
