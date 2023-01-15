from math import pow
from math import sqrt
from random import randint
from turtle import color
from turtle import colormode
from turtle import exitonclick
from turtle import forward
from turtle import left
from turtle import right
from turtle import setposition


def draw_house(size):
    roof = sqrt(2 * pow(size / 2, 2))
    roof_third = roof / 3
    chimney_roof = size / 6
    cross = sqrt(2 * pow(size, 2))

    forward(size)
    left(90)
    forward(size)
    left(45)

    forward(roof_third)
    right(45)
    forward(size / 2)
    left(90)
    forward(chimney_roof)
    left(90)
    forward(size / 2 - chimney_roof)
    right(135)
    forward(roof_third)
    left(90)

    forward(roof)
    left(45)
    forward(size)
    left(135)

    forward(cross)
    left(135)
    forward(size)
    left(135)
    forward(cross)
    left(45)


colormode(255)
setposition(-400, 0)

i = 1
house_number = 10
while i <= house_number:
    color(randint(0, 255), randint(0, 255), randint(0, 255))
    draw_house(randint(20, 100))
    if i != house_number:
        color(0, 0, 0)
        forward(10)
    i += 1

exitonclick()
