Bill = int(input("Enter the amount of bill: "))
Tip = int(input("Enter the percentage of Tip : 12 , 8, 6, or 2: "))
Split = int(input("How many people are splitting the bill: "))
tip_percent= Tip / 100
Amount = (Bill * tip_percent)
Bill_per_person = (Amount / Split)
Final_amt = round(Bill_per_person , 2)
Final_amt = "{:.2f}".format(Bill_per_person)
print(f"Each person should pay: ${Final_amt}")