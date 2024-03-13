import turtle

window = turtle.Screen()
window.title("Lab 1")
window.setup(width=1000, height=1000)

pen = turtle.Turtle()

pen.up()
pen.goto(0, 0)
pen.down()

#Draw the rectangle
pen.forward(250) 
pen.right(90)
pen.forward(100)
pen.right(90)
pen.forward(250)
pen.right(90)
pen.forward(100)

pen.hideturtle()

turtle.done()