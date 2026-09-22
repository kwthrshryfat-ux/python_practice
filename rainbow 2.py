import turtle
import colorsys

screen = turtle.Screen()
screen.bgcolor("black")
screen.colormode(255)
screen.title("rainbow 🌈")

t = turtle.Turtle()
t.speed(0)
t.width(3)
t.hideturtle()

hue = 0

while True:
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)

    t.pencolor(int(r * 255), int(g * 255), int(b * 255))

    t.forward(200)
    t.right(171)

    hue += 0.01
    if hue >= 1:
        hue = 0

turtle.done()
        
