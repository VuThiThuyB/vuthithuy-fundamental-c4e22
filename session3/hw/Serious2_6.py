print("Hello, my name is Thuy and these are my ship sizes")
sheeps = [5, 7, 300, 90, 24, 50, 75]
print(sheeps)

print("Now my biggest sheep has size",max(sheeps),"let's shear it")

print("After shearing, here is my flock ")
index = sheeps.index(max(sheeps))#sheeps.index(giá trị x): tìm vị trí của giá trị x trong list sheeps
sheeps[index] = 8
print(sheeps)



for i in range(2):
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

print("MONTH 3:\n")
for i in range(len(sheeps)):
    sheeps[i] += 50
print("One month has passed , now here is my flock: \n",sheeps)

s = 0
for j in range(len(sheeps)):
    s += sheeps[j]
    print("My flock has size in total: ",s)

print("I would get: ",s,"*2$ = ",s*2)

