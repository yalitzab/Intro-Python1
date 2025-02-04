#### Week 3 Lecture

#This week, we are covering: 
#Using if, else, and elif statements to make decisions. 
#Comparison operators (>, <, ==, !=, >=, <=) to compare values. 
#Formatting output with f-strings to include variables and perform calculations within strings. 

### > < == != >= <=

#if statement: 
    #this line first 
    #this line second
    #lets and losts of lines
    
#if 8 > 10: 
    #print ("statement was true")
    #print("another line")
    
#print("hello world")

###Ask name and if age is over 18 print you are an adult
first_name = input("What is your first name? ")
age = int(input("What's your age? "))

if age >= 18: 
    print("You are an adult!")
    
name = input("What is your name?")
if name == "Adam":
    print("You have a great name")

### Ask for a number > = < to 10
num = int(input("Pick a number"))
if num < 10:
    print(num,"You selected a number less than 10.")
if num > 10:
    print(num,"You selected a number greater than 10.")
if num == 10:
    print(num,"You selected a number equal to 10.")

##else statement
num = int(input("Give me a number: "))
if num > 0:
    print("That number is a positive number")
else: 
    print("That number is a negative")


#Weather 72 > is a warm day 72< is a cool day
temp = int(input("What is the temerature? "))
if temp >= 72:
    print("It is a warm day.")
else: 
    print("It is a cool day.")


#### The Discount Price
##Ask for original dicount price
original_price = float(input("What is the original price of the item?"))
give_discount = input("Would you like to apply a discount? (y/n)")
## Would you like to apply a discount 
if give_discount == "y":
    #if yes apply discount
    discount = float(input("Enter the discount percentage: (e.g., 20 for 20%)"))
    discount_amount = (discount / 100) * original_price
    
else:
    discount_amount = 0

final_price = original_price - discount_amount
print("Final price $", final_price)

##add elif statement    
if statement:
    statement goes here
    statement goes here
elif statement:
    statement goes here
    statement goes here
elif statement:
    add more;
else:
    statement goes here
    statement goes here
print("end of program")

score = int(input("What score did you get on your test?"))
#90 to 100 is an A
#80 to 89 is a B
#70 to 79 is a C
#60 to 69 is a D 
#50 or below is an F

if score >= 90:
    print("You got an A!")
elif score >= 80:
    print("You got a B!")
elif score >= 70:
    print("You got a C!")
elif score >= 60:
    print("You got a D!")   
else:
    print("You got an F")
    
if score == 100:
    print("Congrats getting a perfect score!")

print("End program")

####
name = input("What is your name? ")
age = int(input("What is you age? "))
    
print("Hello", name, "you are", age, "years old")
print("print this out")
