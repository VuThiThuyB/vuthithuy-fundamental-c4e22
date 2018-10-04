while True:
    yob_str = input("Enter your year of birth : ")

    #print(yob_str.isdigit())# isdigit(): kt xem co phai la so k 
    if yob_str.isdigit():
        yob = int(yob_str)
        age = 2018 - yob
        print(age)
        break
    else:
        print("Not a number")