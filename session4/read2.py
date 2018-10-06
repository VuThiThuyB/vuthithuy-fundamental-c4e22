# tao 1 dictionary
# hoi nguoi dung key
# in ra value cua key

person={
    'name' : 'Thuy',
    'age' : 21,
}
# key = input("What key ")
# value = person[key]
# print(value)

key = input("What key ")
if key in person:  #kiem tra key cos o trong person hay k
    # if key not in person:  kiem tra key cos k lam trong person hay k 
    value = person[key]
    print(value)
else:
    print("Not found")


