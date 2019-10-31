from tkinter import *
from random import randrange as rnd, choice
import time
root = Tk()
root.geometry('800x600')
n = 0
dt = 0.1
canv = Canvas(root, bg = 'white')
canv.pack(fill = BOTH, expand = 1)
colors = ['red', 'orange', 'yellow', 'green', 'blue']

x = rnd(100, 700)
y = rnd(100, 500)
r = rnd(30, 50)
if choice([True, False]):
    v1 = rnd(5, 7)
else:
	v1 = rnd(-7, -5)
if choice([True, False]):
    v2 = rnd(5, 7)
else:
    v2 = rnd(-7, -5)
color = choice(colors)


def move_ball():
    global x, y, v1, v2
    canv.delete(ALL)
    canv.create_oval(x - r, y - r, x + r, y + r, fill = color, width = 0)
    x = x + v1 * dt
    y = y + v2 * dt
    if (x + r) > 800 or (x - r) < 0:
       v1 =- v1
    if (y + r) > 600 or (y - r) < 0:
        v2 =- v2
    root.after(1, move_ball)


def click(event):
    global n
    print(event.x, event.y)
    if (x - event.x)**2 + (y - event.y)**2 > r**2:
        print('промах')
    else:
	    print('попадание')
	    n += 1
    print(n)


move_ball()
canv.bind('<Button-1>', click)
mainloop()
