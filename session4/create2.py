film = {
    "name" : "A",
    "time" : 22,
}
#hỏi người dùng nhập vào key và value của key
# key = input("name's new key : ")
# value = input("value's new key : ")
# film[key] = value
# print(film)

text = input("Enter new item: ")
pair = text.split(",")
key = pair[0] 
value = pair[1]
#cachs viet tat cho  key = pair[0]  value = pair[1] la :    key,value = pair

film[key] = value
print(film)
