print("welcome to the tip calculator")
bill = float(input("what was the total bill $"))
tip = int(input("what percentage tip would you like to give? 10,12 or 15 " ))
people =int(input("how many people to split the bill?"))
tip_as_percent = tip/100
tip_amount = tip_as_percent*bill
total_bill = tip_amount + bill
bill_per_person = total_bill/people

print(bill_per_person)
