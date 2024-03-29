import turtle
from PIL import Image

turtle.setup(650, 350, 200, 200)
turtle.penup()
turtle.forward(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("purple")
turtle.seth(-40)
for i in range(4):
    turtle.circle(40, 80)
    turtle.circle(-40, 80)
turtle.circle(40, 80 / 2)
turtle.forward(40)
turtle.circle(16, 180)
turtle.forward(40 * 2 / 3)

ts = turtle.getscreen()
ts.getcanvas().postscript(file=r"circle.eps")

cc = Image.open("circle.eps")
cc.save("circle.jpg", "JPEG")