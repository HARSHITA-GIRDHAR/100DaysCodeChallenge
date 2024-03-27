import turtle
screen = turtle.Screen()
screen.bgcolor("white")

# Create a new turtle and set its speed to the fastest possible
pen = turtle.Turtle()
pen.speed(0)


pen.fillcolor("red")
pen.begin_fill()


pen.circle(100)


pen.end_fill()
pen.hideturtle()

turtle.done()

