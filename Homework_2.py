##### Assignment 2

###The Pizza Party
# people_count = int(input("How many people are at the party? " ))
# pizza_count = int(input("How many pizzas they ordered? "))
# pizza_slices = int(input("How many slices each pizza has? "))
# total_pizza_slices = pizza_count * pizza_slices
# person_pizza_slice = total_pizza_slices // people_count
# leftover_pizza_slices = total_pizza_slices % person_pizza_slice
#
# print ("There are", people_count, "people at the party.")
# print ("You ordered", pizza_count, "pizzas with", pizza_slices, "slices each.")
# print ("Each person gets", person_pizza_slice, "slices.")
# print ("There are", leftover_pizza_slices, "slices left over")


### The Travel Calculator
# miles = float(input("How far will you be traveling (in miles)? "))
# mpg = float(input("What is your cars fuel efficiency (in miles per gallon)? "))
# gas_price = float(input("What is the current price of gas per gallon? "))
# trip_cost = (miles / mpg) * gas_price
#
# print ("You are traveling", miles, "miles.")
# print ("Your car get", mpg, "miles per gallon.")
# print ("Gas costs $", gas_price, "per gallon.")
# print ("Your trip will cost $", trip_cost)


### The Candy Store
candy_cost = int(input("Enter the price of one piece of candy"))
candy_amount = float(input("How many pieces of candy do you want to buy?"))
total_candy_cost = candy_cost * candy_amount

print ("Each piece of candy costs $", candy_cost)
print ("You want to buy", candy_amount, "pieces.")
print ("The total cost is", total_candy_cost)


###Age in Dog Years
human_age = int(input("What is your age?"))
dog_age = 7
dog_age_years = human_age * dog_age

print ("You are", human_age, "years old.")
print ("In dog years, you are", dog_age_years, "years old.")


### The Discount Price
original_price = float(input("What is the original price of the item?"))
discount_percentage = float(input("Enter the discount percentage: (e.g., 20 for 20%)"))
total_discounted_price = original_price - (original_price * discount_percentage)

print ("The original price is $", original_price)
print ("The discount is", discount_percentage, "%")
print ("The discounted price is $", total_discounted_price)

#Second option
original_price = float(input("What is the original price of the item?"))
discount = float(input("Enter the discount percentage: (e.g., 20 for 20%)"))

final_price = ((100 - discount) / 100) * original_price
#discount_amount = (discount / 100) * original_price
#final_price = original_price - discount_amount

print ("The original price is $", original_price)
print ("The discount is", discount, "%")
print ("The discounted price is $", final_price)

