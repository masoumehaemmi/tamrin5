import turtle
import time

t=turtle.Turtle()
t.shape("turtle")
forwar=20
lef=30
color =["pink","purple","orange","yellow","green","blue",]
azlla =[3 , 4, 5, 6, 7]
angles= [120, 90, 77 ,60 ,50 ]

for i in range (5):
    t.pencolor(color[1%5])
    
    for j in azlla:
    
        t.forward(100)
        t.left(angles[i])
       

t.pendown()
t.setpos(lef ,3* forwar)
t.penup()

time.sleep(3)