import colorgram
import turtle
import random
turtle.colormode(255)

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)

colors_lst = []
for color in rgb_colors:
    t = {color.r, color.g, color.b}
    colors_lst.append(t)

#Pop background colors from list
colors_lst.pop(0)
colors_lst.pop(0)
colors_lst.pop(0)
print(colors_lst)

distance = 30
t = turtle.Turtle()
# start_x = t.xcor()
# start_y = t.ycor()
start_y = -100.0
start_x = -100.0
t.penup()
t.hideturtle()
t.speed('fastest')
for i in range(10):
    t.setx(start_x)
    t.sety(start_y + i * distance)
    for _ in range(10):
        t.forward(distance)
        t.dot(20, random.choice(colors_lst))

screen = turtle.Screen()
screen.exitonclick()
