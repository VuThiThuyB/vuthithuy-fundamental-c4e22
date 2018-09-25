from turtle import *
for i in range(4):
    if i%2==0:
        color("red","white")
        begin_fill()
        for j in range(6-i):
            forward(100) 
            left(360/(6-i))
        end_fill()
    else:
        color("blue","white")
        begin_fill()
        for j in range(6-i):
            forward(100) 
            left(360/(6-i))
        end_fill()
mainloop() 