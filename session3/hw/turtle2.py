from turtle import *

colors = ["red","blue","brown","yellow","gray"]

for i in range(0,5):
    color(colors[-i-1],colors[-i-1]) # mau t1 để vẽ màu khung, màu t2 để cả khung là màu đó 
    begin_fill()
    forward(50*(5-i))
    left(90)
    forward(100)
    left(90)
    forward(50*(5-i))
    left(90)
    forward(100)
    left(90)
    end_fill()
mainloop()