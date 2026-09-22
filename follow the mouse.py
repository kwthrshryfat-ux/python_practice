import turtle

screen = turtle.Screen()
screen.bgcolor("skyblue")
screen.title("follow the mouse")

t = turtle.Turtle()
t.shape("turtle")
t.color("black")
t.speed(3)

def go_to_click(x, y):
    t.goto(x, y)

screen.onclick(go_to_click)\

turtle.done()
    