import turtle
wn = turtle.Screen()

elan = turtle.Turtle()

distance = 5
an=90
for _ in range(500):
    elan.forward(distance)
    elan.right(an)
    an=an-.5
    distance = distance + .5
