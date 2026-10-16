import turtle
import math
xc = float(input("xc = "))
yc = float(input("yc = "))
r = float(input("r = "))
x = float(input("x = "))
y = float(input("y = "))

dist = math.hypot(x - xc, y - yc)
screen = turtle.Screen()
t = turtle.Turtle()

t.speed(0)
t.penup()
t.goto(xc, yc - r)
t.pendown()
t.circle(r)
t.penup()

t.goto(x, y)
t.pendown()
t.dot(10, "red")

if dist < r:
    text = "Точка внутри окружности"
elif dist > r:
    text = "Точка вне окружности"
else:
    text = "Точка на окружности"

t.penup()
t.goto(xc, yc - r - 20)
t.pendown()
t.color("red")
t.write(text, align="center", font=("Arial", 9, "normal"))

turtle.done()