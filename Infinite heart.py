import turtle
import math

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("infinite heart")
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.width(3)

angle = 0

def heart_position(t_param, scale):

    x = 16 * (math.sin(t_param) ** 3)
    y = (13 * math.cos(t_param) - 5 * math.cos(2 * t_param) - 2 * math.cos(3 * t_param) - math.cos(4 * t_param))
    return x * scale, y * scale

def draw_heart(scale, color):
    t.pencolor(color)
    t.penup()
    first = True
    steps = 200
    for i in range(steps + 1):
        angle_t = i * (2 * math.pi / steps)
        x, y = heart_position(angle_t, scale)
        if first:
            t.goto(x, y -50)
            t.pendown()
            first = False
        else:
            t.goto(x, y - 50)
    t.penup()

def pulse():
    global angle
    t.clear()
    scale = 10 + 1.5 * math.sin(angle)
    color = "red" if math.sin(angle) > 0 else "pink"
    draw_heart(scale, color)
    screen.update()
    angle += 0.2
    screen.ontimer(pulse, 50)

pulse()
screen.mainloop()
    
