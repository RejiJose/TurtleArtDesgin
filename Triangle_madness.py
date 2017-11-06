import turtle
from Mydesgin import * #calls in another file.
turtle.colormode(255)#RGB color format.
turtle.bgcolor("black") #makes background black.

bob=turtle.Turtle()
bob.speed(0)#sets the speed of bob aka(turtle)

for times in range(250):
    bob.color(times,50,100)
    polygon(bob,50,3)
    bob.penup()#moves the penup so lines do not form.
    bob.forward(times)
    bob.left(50)
    bob.pendown()#moves pen down so lines do not form.



bob.penup()
bob.goto(600,300)
bob.pendown()
for times in range(390):
    bob.color(100,155,0)
    polygon(bob,50,3)
    bob.penup()
    bob.forward(times)
    bob.left(50)
    bob.pendown()



bob.penup()
bob.goto(-600,300)
bob.pendown()
for times in range(400):
    bob.color(100,55,80)
    polygon(bob,50,3)
    bob.penup()
    bob.forward(times)
    bob.left(50)
    bob.pendown()

bob.penup()
bob.goto(600,-350)
bob.pendown()


for times in range(420):
    bob.color(0,100,155)
    polygon(bob,50,3)
    bob.penup()
    bob.forward(times)
    bob.left(50)
    bob.pendown()
bob.penup()
bob.goto(-500,-300)
bob.pendown()
for times in range(450):
    bob.color(255,0,0)
    polygon(bob,50,3)
    bob.penup()
    bob.forward(times)
    bob.left(50)
    bob.pendown()

























    




    
        
    






