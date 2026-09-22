import turtle
import random

screen = turtle.Screen()
screen.bgcolor("white")
screen.title("number guessing visualizer")
screen.setup(width=500, height=500)

t = turtle.Turtle()
t.hideturtle()
t.penup()

target = random.randint(1, 100)
attempts = 0
max_attempts = 7

def show_message(text, color="black", y=0):
    t.goto(0, y)
    t.color(color)
    t.write(text, align="center", font=("Arial", 16, "bold"))

def check_guess():
    global attempts
    guess = screen.textinput("حدس بزن", f"یه عدد بین ۱ تا ۱۰۰ حدس بزن (تلاش {attempts+1} از {max_attempts}):")

    if guess is None:
        turtle.bye()
        return

    if not guess.isdigit():
        t.clear()
        show_message("لطفاً فقط عدد وارد کن!", "red")
        screen.ontimer(check_guess, 1000)
        return

    guess = int(guess)
    attempts += 1
    t.clear()

    if guess == target:
        show_message(f"🎉 آفرین! عدد درست بود: {target}", "green")
        show_message(f"تعداد تلاش‌ها: {attempts}", "black", -40)
    elif attempts >= max_attempts:
        show_message(f"❌ تلاش‌هات تموم شد! عدد درست {target} بود.", "red")
    else:
        hint = "بزرگ‌تره ⬆️" if guess < target else "کوچیک‌تره ⬇️"
        show_message(f"غلطه! عدد درست {hint}", "orange")
        screen.ontimer(check_guess, 800)

check_guess()
turtle.done()
        