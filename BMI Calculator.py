height = input("Enter your height")
weight = input ("Enter your weight")

bmi = float(weight) / float(height) **2
bmi_as_int = int(bmi)
print(bmi_as_int)