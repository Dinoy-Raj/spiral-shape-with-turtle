import turtle
wn = turtle.Screen()
wn.bgcolor("green")

elan = turtle.Turtle()
elan.color("blue")
elan.shape("turtle")
elan.speed(20)
elan.pensize(3)
elan.up()
distance = 5
an=24
for _ in range(70):
    elan.stamp()
    elan.forward(distance)
    elan.right(an)

    distance = distance + 2
wn.exitonclick()
