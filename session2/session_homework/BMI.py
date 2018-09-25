h = float(input("Your height : "))
w = float(input("Your weight : "))
h1 = h/100

BMI = w/(h1*h1)
print(BMI)

if BMI < 16:
    print("Severely underweight")
elif 16 <= BMI < 18.5:
    print("Underweight")
elif 18.5 <= BMI < 25:
    print("Normal")
elif 25 <= BMI <= 30:
    print("Overweight ")
else:
    print("Obese")
    