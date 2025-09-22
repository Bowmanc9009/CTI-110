# Charles Bowman
# 9/22/25
# P1HW2
# Calculating and displayingn travel budget

# input budget
budget = int( input("Enter your budget: ") )
# input destination
goal = input("Enter your destination: ")
# input gas expenses
gas = int( input("Enter how much you will spend on gas: ") )
# input accomodation expenses 
accom = int( input("Enter how much you will spend on accomodations: ") )
# input food expenses
food = int( input("Enter how much you will spend on food: ") )
# calculate result
result = budget - ( gas + accom + food) 
print ("---------------Travel Expenses--------------")
# Display destination
print("Location: ", goal)
# Display budget
print ("Budget: ", budget)
# Display gas price
print("Gas: ", gas)
# Display accomodation expenses
print("accomodations:", accom)
# Display food expenses
print("Food: ", food)
# Display remaining balance
print("Remaining Balance: ", result)

