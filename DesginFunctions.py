def square(t, dist):
    for times in range(4):
        t.forward(dist)
        t.left(90)

def triangle(t, dist):
    for times in range(3):
        t.forward(dist)
        t.left(120)

def pentagon(t, dist):
    for times in range(5):
        t.forward(dist)
        t.left(72)

def hexagon(t, dist):
    for times in range(6):
        t.forward(dist)
        t.left(60)

def dodecagon(t, dist):
    for times in range(12):
        t.forward(dist)
        t.left(30)
#defines the fuction "polygon"
def polygon(t, dist, sides):
    angle = 360/sides
    t.begin_fill()
    for times in range(sides):
        t.forward(dist)
        t.left(angle)
    t.end_fill()
def star(t, dist):
    for times in range(5):
        t.forward(dist)
        t.left(144)
def jump(t,x,y):
        t.penup()
        t.goto(x,y)
        t.pendown()
    
