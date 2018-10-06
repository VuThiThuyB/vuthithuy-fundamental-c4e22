person = {
    'name':'Thuy',
    'age':21,
    'location': 'Hanoi'
}

#in ra key
# for x in person:
#     print(x)  # in ra key


# #in ra value
# for v in person.values():
#     print(v)

# #in ra cả key và value
# for k in person.keys():  # for k in person:  (dùng cũng đc )
#     # print(k)
#     # print(person[k]) # in ra value
#     print(k,person[k])  # cách viết tắt của 2 dòng lệnh trên




#in cả key và value
for k,v in person.items():
    print(k,v,sep=":")

