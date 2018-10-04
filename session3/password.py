while True:
    password = input("Enter your password : ")
    
   # if len(password) <= 8 :
       # print("Not long enought")
   # elif password.isdigit():#chi co so
        #print("Must not contain only digits")
    #elif password.isupper():#cho co chu hoa
        #print("Must contain lowercase letters")
    #elif password.islower():#chi co chu thuong
        #print("Must contain uppercase letters")
    #else:
        #print("OK")
       # break
    if len(password) >= 8 & password.isdigit == False & password.isupper == False & password.islower == False:
        print(password)
        break
    else:
        print("Not password")