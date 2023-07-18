name = input("hello what is your name? : ")
print("nice to meet you " + name)
age = int(input("how old are you? : "))
age = age + 1 
print("Happy birthday and congratualtions on turning to "+ str(age) + " old today ")

#here we are taking data from the user
#lets learn the flow of it 
#we first take soem input from the user 
#then we tell the computer that input is the users name 
# then we treat name as a variable and print a message while using the answer as a strg variable 
# in the next step we don exatly same but we try to add one to the users age 
# but the input is a strg and we need either int or a float to do the maths 
#hence we tell the computer to treat the input as an int 
#in the next step we let the computer use the age as an int to perform math 
# now we need to give out an output hence we will have to change the age intr back to a strn 
# so we tell computer to treat it as a str again using type casting. 
# and boom its done.
current_age = float(input("what is your age today? :"))
current_age = current_age + 10/12
print("after 10 months you will be  "+ str(current_age)+ " years old")
#here we are making a very baisc age calculator which adds 1 year to your current age.
#chapter concluded.