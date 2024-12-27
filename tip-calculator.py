total_bill = int(input("What was the total bill?\n"))
tip_amount = int(input("What is the tip you want to add as a percentage?\n"))
total_number_of_peoples = int(input("total number of peoples bill to be split?\n"))
tip_percentage = (tip_amount * total_bill)/100
final_bill = (total_bill + tip_percentage)/total_number_of_peoples
print("The final bill per each person is : "+ str(round(final_bill, 2)))
