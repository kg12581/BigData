# 以下是几种常见的圣诞树代码：

# Python
# turtle库绘制圣诞树
#
# python

import turtle as t
from turtle import *
import random as r


if __name__ == '__main__':
        n = 100.0
        t.speed(1000)
        t.pensize(5)
        t.screensize(800, 800, bg='black')
        t.left(90)
        t.forward(250)
        t.color("orange", "yellow")
        t.begin_fill()
        t.left(126)
        for i in range(5):
            t.forward(n / 5)
            t.right(144)
            t.forward(n / 5)
            t.left(72)
        t.end_fill()
        t.right(126)


        def drawlight():
            if r.randint(0, 50) == 0:
                t.color('tomato')
                t.circle(3)
            elif r.randint(0, 30) == 1:
                t.color('orange')
                t.circle(4)
            elif r.randint(0, 50) == 2:
                t.color('blue')
                t.circle(2)
            elif r.randint(0, 30) == 3:
                t.color('white')
                t.circle(4)
            else:
                t.color('darkgreen')


        def tree(d, s):
            if d <= 0:
                return
            t.forward(s)
            tree(d - 1, s * .8)
            t.right(120)
            tree(d - 3, s * .5)
            drawlight()
            t.right(120)
            tree(d - 3, s * .5)
            t.right(120)
            t.backward(s)


        tree(15, 100)
        t.backward(50)
        for i in range(200):
            a = 200 - 400 * r.random()
            b = 10 - 20 * r.random()
            t.up()
            t.forward(b)
            t.left(90)
            t.forward(a)
            t.down()
            if r.randint(0, 1) == 0:
                t.color('tomato')
            else:
                t.color('wheat')
            t.circle(2)
            t.up()
            t.backward(a)
            t.right(90)
            t.backward(b)

        t.up()
        t.goto(100, 200)
        t.down()
        t.color("darkred", "red")
        t.penup()
        t.write("christmastree", font=("comicsansms", 16, "bold"))


