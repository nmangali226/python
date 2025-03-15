## This script will split bill accross members

# Total bill for the dinner
total_bill = int(input("What was the total bill?\n"))

#tip amount you want to add
tip_amount = int(input("What is the tip you want to add as a percentage?\n"))

#number of peoples you want to split across
total_number_of_peoples = int(input("total number of peoples bill to be split?\n"))

# Calculating tip percentage over the total bill
tip_percentage = (tip_amount * total_bill)/100

#calculating final bill for each person
final_bill = (total_bill + tip_percentage)/total_number_of_peoples

#round figure the total amount to 2 decimals
rounded_bill = round(final_bill, 2)

# Print the final bill for everyone
print(f"The final bill per each person is :  {rounded_bill}")
