print("Hello, my name is Thuy and these are my ship sizes")
sheeps = [5, 7, 300, 90, 24, 50, 75]
print(sheeps)
print("Now my biggest sheep has size",max(sheeps),"let's shear it")
print("After shearing, here is my flock ")
sheeps.pop(sheeps.index(max(sheeps)))
#sheeps.index(giá trị x): tìm vị trí của giá trị x trong list sheeps
sheeps[sheeps.index(max(sheeps))] = 8
print(sheeps)