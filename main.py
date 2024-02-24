import turtle as t
import random

mason = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

random_color()

mason.shape("arrow")
mason.color("black")
mason.speed(15)

for _ in range(72):
    mason.color(random_color())
    mason.circle(100)
    mason.left(5)




t.exitonclick()
