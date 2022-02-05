from tkinter import *
import random

window = Tk()
window.title('Zmeyaaaaaaa')
WIDTH = 600
HIGHT = 600
RASSTOYANIE = 40


def kraska(X, Y, cvet="green"):
    X_P1 = X * RASSTOYANIE + 2
    Y_P1 = Y * RASSTOYANIE + 2
    X_P2 = (X + 1) * RASSTOYANIE
    Y_P2 = (Y + 1) * RASSTOYANIE
    canvas.create_rectangle(X_P1, Y_P1, X_P2, Y_P2, fill=cvet)


current_x = 5
current_y = 5

apple_position = [-1, -1]

zmeya = [(current_x, current_y)]


def w(event):
    global current_y
    zmeya[0] = (current_x, current_y)
    current_y -= 1
    if current_x == apple_position[0] and current_y == apple_position[1]:
        zmeya.insert(0, (current_x, current_y))
        kraska(current_x, current_y)
        apple()
        return 0
    else:
        kraska(current_x, current_y, cvet="black")
    if current_y < 0:
        current_y = HIGHT // RASSTOYANIE - 1
    kraska(zmeya[-1][0], zmeya[-1][1], cvet="black")
    zmeya.pop()
    zmeya.insert(0, (current_x, current_y))
    kraska(current_x, current_y)


def s(event):
    global current_y
    zmeya[0] = (current_x, current_y)
    if len(zmeya) > 1 and current_y + 1 == zmeya[1][1]:
        return 0
    current_y += 1
    if current_x == apple_position[0] and current_y == apple_position[1]:
        zmeya.insert(0, (current_x, current_y))
        kraska(current_x, current_y)
        apple()
        print(zmeya)
        return 0
    else:
        kraska(current_x, current_y, cvet="black")
    if current_y >= HIGHT // RASSTOYANIE:  # выход за границу поля
        current_y = 0
    kraska(zmeya[-1][0], zmeya[-1][1], cvet="black")
    zmeya.pop()
    zmeya.insert(0, (current_x, current_y))
    kraska(current_x, current_y)


def a(event):
    global current_x
    zmeya[0] = (current_x, current_y)
    if len(zmeya) > 1 and current_x - 1 == zmeya[1][1]:
        return 0
    current_x -= 1
    if current_x == apple_position[0] and current_y == apple_position[1]:
        zmeya.insert(0, (current_x, current_y))
        kraska(current_x, current_y)
        apple()
        print(zmeya)
        return 0
    else:
        kraska(current_x, current_y, cvet="black")
    if current_x >= HIGHT // RASSTOYANIE:  # выход за границу поля
        current_x = 0
    kraska(zmeya[-1][0], zmeya[-1][1], cvet="black")
    zmeya.pop()
    zmeya.insert(0, (current_x, current_y))
    kraska(current_x, current_y)


def d(event):
    global current_x
    zmeya[0] = (current_x, current_y)
    if len(zmeya) > 1 and current_x - 1 == zmeya[1][1]:
        return 0
    current_x += 1
    if current_x == apple_position[0] and current_y == apple_position[1]:
        zmeya.insert(0, (current_x, current_y))
        kraska(current_x, current_y)
        apple()
        return 0
    else:
        kraska(current_x, current_y, cvet="black")
    if current_x < 0:
        current_x = HIGHT // RASSTOYANIE - 1
    kraska(zmeya[-1][0], zmeya[-1][1], cvet="black")
    zmeya.pop()
    zmeya.insert(0, (current_x, current_y))
    kraska(current_x, current_y)


def apple():
    apple_position[0] = random.randint(0, WIDTH // RASSTOYANIE - 1)
    apple_position[1] = random.randint(0, HIGHT // RASSTOYANIE - 1)
    kraska(apple_position[0], apple_position[1], cvet="white")


canvas = Canvas(window, width=WIDTH, height=HIGHT, bg="black", cursor="pencil")
for i in range(1, HIGHT, RASSTOYANIE):
    canvas.create_line(0, i, WIDTH, i, width=1, fill="grey")
for i in range(1, WIDTH, RASSTOYANIE):
    canvas.create_line(i, 0, i, HIGHT, width=1, fill="grey")

kraska(current_x, current_y)

apple()

window.bind("w", w)
window.bind("s", s)
window.bind("a", a)
window.bind("d", d)
canvas.pack()
window.mainloop()
