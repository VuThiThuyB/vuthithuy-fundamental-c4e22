items = ["Ha Noi","Dan Nang","Nha Trang","Da Lat"]
print(*items,sep=", ")
#new_item = input("Diem du lich noi tieng muon den : ")
#items.append(new_item)
#print(*items,sep="\n")

#
#while True:
    #a = (input("Vi tri muon xem la : "))
    #if a.isdigit():
        #if a<len(*items):
           # print(items[a-1])
            #break
        #else:
            #print("Khong thoa man")
    #else:
        #print("Khong thoa man")

#update
a = int(input("Ban muon thay doi o dau :"))
str = input("Noi dung thay doi la : ")
items[a-1] = str
print(items)

#delete
d = input("ban muon xoa gi : ")
if d.isdigit():
    d1 = int(d)
    items.pop(d1-1)
    print(items)
else:
    items.remove(d)
    print(items)
