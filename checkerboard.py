import turtle

screen = turtle.Screen()
screen.bgcolor("white")
screen.title("checkerboard")

t = turtle.Turtle()
t.speed(0)
t.penup()

square_size = 40
rows = 8
cols = 8

start_x = -160
start_y = -160


for row in range(rows):
    for col in range(cols):
        x = start_x + col * square_size
        y = start_y + row * square_size

        t.goto(x, y)
        t.pendown()


        if (row + col) % 2 == 0:
            t.fillcolor("black")
        else:
            t.fillcolor("white")

        t.begin_fill()
        for _ in range(4):
            t.forward(square_size)
            t.left(90)

            
        t.end_fill() 
        t.penup()

t.hideturtle()
turtle.done()
                 