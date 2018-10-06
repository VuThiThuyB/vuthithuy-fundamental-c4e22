person = {
        'name':'Thuy',
        'age':21,
        'class':'JS1104',
    }
    #1
    print(person)
    a = input("Bạn muốn xóa hay cập nhật(D/U): ")

    if a == 'D':
        key = input("Tên key muốn xóa là : ")
        if key not in person:
            print("Not found")
        else:
            del person[key]
            print(person)
    elif a == "U":
        key = input("muốn cập nhật cái gì : ")
        value = input("New info : ")
        person[key] = value
        print(person)