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


