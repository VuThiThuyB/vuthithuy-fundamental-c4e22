print("Hello, my name is Thuy and these are my ship sizes")
sheeps = [5, 7, 300, 90, 24, 50, 75]
print(sheeps)

for i in range(4):
    print("MONTH ",(i+1))
    for j in range(len(sheeps)):
        sheeps[j] += 50

    print("One month has passed, now here is my flock \n",sheeps)

    print("Now my biggest sheep has size",max(sheeps),"let's shear it")

    print("After shearing, here is my flock ")
    index = sheeps.index(max(sheeps))#sheeps.index(giá trị x): tìm vị trí của giá trị x trong list sheeps
    sheeps[index] = 8
    print(sheeps)
    new_sheeps = sheeps
    




