while True:
   a = input("Welcome to our shop, what do you want (C, R, U, D)? : ")
   items = ["T-Shirt","Sweater"]
   crud = ["C","R","U","D"]
   if a == crud[0]:
       new_item = input("Enter new item: ")
       items.append(new_item)
       print("our items : ",*items,sep=", ")
       new_items = items
   elif a == crud[1]:
        print("Our items: ",*items)
   elif a == crud[2]:
        b = int(input("Update posotion? "))
        str = input("New item? ")
        new_items[b-1] = str
        print("Our items: ",*new_items,sep=", ")
   elif a == crud[3]:
        c = input("Delete position? ")
        if c.isdigit():
            c1 = int(c)
            new_items.pop(c1-1)
            print("Our items: ",*new_items,sep="")
        else:
            new_items.remove(c)
            print("Our items: ",*new_items,sep=", ")
        break


        
        

   
    
    #elif a == crud[2]:
       # b = int(input("Update position? "))
        #str = input("New item? ")
        #items[b-1] = str
        #print(*items)
        
       
