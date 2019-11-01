from tkinter import *
from random import randrange as rnd, choice
import math
import time

"""Параметры окна"""
root = Tk()
root.geometry('800x600')

canv = Canvas(root, width=800, height=600, bg='#C0C0C0')
canv.pack(fill=BOTH, expand=1)


colors = ['red', 'orange', 'yellow', 'green', 'blue']
colors2 = ['#FFA07A', '#90EE90', '#FFDEAD', '#7B68EE', '#8B0000']
ball = []
square = []
score = [0]


"""Создание списка шариков"""
def new_ball():
    global x, y, r, dx, dy, ball
    """Случайное начальное местположение и радиус шариков"""
    x = [rnd(100, 700)]
    y = [rnd(100, 500)]
    r = [rnd(10, 50)]
    """Диапазон изменения скорости"""
    dx = [rnd(-10, 10)]
    dy = [rnd(-10, 10)]
    """Создание 10 шариков со случайными параметрами из заданных диапазонов"""
    for j in range(10):
        x.append(rnd(100, 700))
        y.append(rnd(100, 500))
        r.append(rnd(10, 50))
        dx.append(rnd(-10, 10))
        dy.append(rnd(-10, 10))
        ball.append(canv.create_oval(x[j] - r[j], y[j] - r[j], x[j] +
        r[j], y[j] + r[j], fill=choice(colors), width=0))

def new_square():
    global x1, y1, h, dx1, dy1, square
    """Случайное начальное местположение и размер"""
    x1 = [rnd(100, 700)]
    y1 = [rnd(100, 500)]
    h = [rnd(30, 60)]
    """Диапазон изменения скорости"""
    dx1 = [rnd(-10, 20)]
    dy1 = [rnd(-10, 20)]
    """Создание 10 квадратов со случайными параметрами из заданных диапазонов"""
    for j in range(10):
        x1.append(rnd(100, 700))
        y1.append(rnd(100, 500))
        h.append(rnd(30, 60))
        dx1.append(rnd(-10, 10))
        dy1.append(rnd(-10, 10))
        square.append(canv.create_rectangle(x1[j], y1[j], x1[j] +
        h[j], y1[j] + h[j], fill=choice(colors2), width=0))


"""Задаёт движение шариков"""
def move_ball():
    for i in range(10):
        canv.move(ball[i], dx[i], dy[i])
        x[i] = x[i] + dx[i]
        y[i] = y[i] + dy[i]
        """Проверяет наличие стен и меняет напраление движения
           на противоположное"""
        if x[i] + r[i] >= 800 or x[i] - r[i] <= 0:
            dx[i] = - dx[i]
        if y[i] + r[i] >= 600 or y[i] - r[i] <= 0:
            dy[i] = -dy[i]
        """Скорость движения"""
    root.after(40, move_ball)

"""Задаёт движение квадратов"""
def move_square():
    for i in range(10):
        canv.move(square[i], dx1[i], dy1[i])
        x1[i] = x1[i] + dx1[i]
        y1[i] = y1[i] + dy1[i]
        """Проверяет наличие стен и меняет напраление движения
           на противоположное"""
        if x1[i] + h[i] >= 800 or x1[i] - h[i] <= 0:
            dx1[i] = - dx1[i]
        if y1[i] + h[i] >= 600 or y1[i] - h[i] <= 0:
            dy1[i] = -dy1[i]
        """Скорость движения"""
    root.after(22, move_square)


"""События, происходящие по клику левой кнопки мыши: при попадании по шарику
он исчезает, в счёт записывается попадание, текущий счёт записывается в файл"""
def click(event):
    """Счётчик попаданий"""

    for i in range(len(ball)):
        if (x[i] - event.x) ** 2 + (y[i] - event.y) ** 2 <= r[i]**2:
            canv.delete(ball[i])
            score[0] += 1
    for i in range(len(square)):
        if (event.x >= x1[i]) and (event.x <= x1[i] + h[i]) and \
           (event.y >= y1[i]) and (event.y <= y1[i] + h[i]):
            canv.delete(square[i])
            score[0] += 3
    """Отображение счётчика попаданий в окне программы"""
    score_label = Label(canv, text= "Счёт: " + str(score[0]),
                  font = "Calibri 18", fg = 'blue')
    score_label.place(x = 0, y = 30)
    """Запись результатов в файл"""
    file = open('players.txt', 'a')
    file.write(user_name + "," + "счёт:" + str(score[0]) + "\n")
    file.close()



"""Окно ввода имени пользователя"""
user_name = input("Имя пользователя: ")

"""Отображение имени пользователя в окне программы"""
user_line = Label(canv, text = "Имя пользователя: " +
                  user_name, font="Calibri 18", fg = 'blue')
user_line.place(x = 0, y = 0)

"""Вызов подпрограмм"""
new_ball()
move_ball()



new_square()
move_square()

canv.bind('<Button-1>', click)


mainloop()