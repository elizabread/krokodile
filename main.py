import time
from tkinter import *
import random

window = Tk()
window.title('snake')

HEIGHT = 600   # высота
WIDTH = 600    # ширина
DISTANCE = 60  # расстояние между полосками в пикселях
SPEED = 1

current_x = random.randint(0, WIDTH // DISTANCE - 1)   # изначальное значение х
current_y = random.randint(0, HEIGHT // DISTANCE - 1)  # изначальное ачение у

apple_position = [-1, -1]  # положение яблока
snake = [(current_x, current_y)]  # массив с положениями ячеек змеи

canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="black", cursor="heart")  # создание поля

for i in range(1, HEIGHT, DISTANCE):
    canvas.create_line(0, i, WIDTH, i, width=1, fill="grey")   # горизонтальные полоски
for i in range(1, WIDTH, DISTANCE):
    canvas.create_line(i, 0, i, HEIGHT, width=1, fill="grey")  # вертикальные полоски


def fill(x, y, colour="green"):  # закрашиваем голову змеи
    x1 = x * DISTANCE + 2    # верхняя грань
    y1 = y * DISTANCE + 2    # левая грань
    x2 = (x + 1) * DISTANCE  # нижняя грань
    y2 = (y + 1) * DISTANCE  # правая грань
    canvas.create_rectangle(x1, y1, x2, y2, fill=colour)


def apple():  # появление яблока
    apple_position[0] = random.randint(0, WIDTH // DISTANCE - 1)  # координата по х
    apple_position[1] = random.randint(0, HEIGHT // DISTANCE - 1)  # координата по у
    while (apple_position[0], apple_position[1]) in snake:  # если яблоко появилось в змее
        apple_position[0] = random.randint(0, WIDTH // DISTANCE - 1)  # меняем позицию яблока
        apple_position[1] = random.randint(0, HEIGHT // DISTANCE - 1)
    fill(apple_position[0], apple_position[1], colour="red")  # закрашиваем яблоко


def w(event):  # нажатие на w
    global current_y
    global NAPRAVLENIE
    NAPRAVLENIE = 0
    # if event != 0:
    #     return 0
    snake[0] = (current_x, current_y)  # записываем в массив координату головы
    if len(snake) > 1 and current_y - 1 == snake[1][1]:  # не даем войти в себя
        return 0
    current_y -= 1  # перемещаем значение вверх
    if current_y < 0:  # если выходим за рамки
        current_y = HEIGHT // DISTANCE - 1  # телепортируемся в противоположный край
    if current_x == apple_position[0] and current_y == apple_position[1]:  # съедаем яблоко
        snake.insert(0, (current_x, current_y))  # записываем вначало массива координаты головы
        fill(current_x, current_y)
        apple()
        return 0
    else:
        fill(current_x, current_y, colour="black")
    fill(snake[-1][0], snake[-1][1], colour="black")
    snake.pop()
    snake.insert(0, (current_x, current_y))
    fill(current_x, current_y)
    game_over()


def s(event):
    global current_y
    global NAPRAVLENIE
    NAPRAVLENIE = 1
    snake[0] = (current_x, current_y)
    # if event != 0:
    #     return 0
    if len(snake) > 1 and current_y + 1 == snake[1][1]:
        return 0
    current_y += 1
    if current_y >= HEIGHT // DISTANCE:  # выход за границу поля
        current_y = 0
    if current_x == apple_position[0] and current_y == apple_position[1]:
        snake.insert(0, (current_x, current_y))
        fill(current_x, current_y)
        apple()
        return 0
    else:
        fill(current_x, current_y, colour="black")
    fill(snake[-1][0], snake[-1][1], colour="black")
    snake.pop()
    snake.insert(0, (current_x, current_y))
    fill(current_x, current_y)
    game_over()


def a(event):
    global current_x
    global NAPRAVLENIE
    NAPRAVLENIE = 2
    snake[0] = (current_x, current_y)
    # if event != 0:
    #     return 0
    if len(snake) > 1 and current_x - 1 == snake[1][0]:
        return 0
    current_x -= 1
    if current_x < 0:  # выход за границу поля
        current_x = WIDTH // DISTANCE - 1
    if current_x == apple_position[0] and current_y == apple_position[1]:
        snake.insert(0, (current_x, current_y))
        fill(current_x, current_y)
        apple()
        return 0
    else:
        fill(current_x, current_y, colour="black")
    fill(snake[-1][0], snake[-1][1], colour="black")
    snake.pop()
    snake.insert(0, (current_x, current_y))
    fill(current_x, current_y)
    window.update()
    game_over()


def d(event):
    global current_x
    global NAPRAVLENIE
    NAPRAVLENIE = 3
    # if event != 0:
    #     return 0
    snake[0] = (current_x, current_y)
    if len(snake) > 1 and current_x + 1 == snake[1][0]:
        return 0
    current_x += 1
    if current_x >= WIDTH // DISTANCE:  # выход за границу поля
        current_x = 0
    if current_x == apple_position[0] and current_y == apple_position[1]:
        snake.insert(0, (current_x, current_y))
        fill(current_x, current_y)
        apple()
        return 0
    else:
        fill(current_x, current_y, colour="black")
    fill(snake[-1][0], snake[-1][1], colour="black")
    snake.pop()
    snake.insert(0, (current_x, current_y))
    fill(current_x, current_y)
    game_over()


def game_over():
    if snake.count(snake[0]) > 1:
        canvas.create_text(WIDTH // 2, HEIGHT // 2, text="Игра окончена!!!", font="Verdana 40", justify=CENTER, fill="red")
        window.update()
        time.sleep(3)
        exit()


apple()
fill(current_x, current_y)

NAPRAVLENIE = 0

window.bind("w", w)
window.bind("s", s)
window.bind("a", a)
window.bind("d", d)
print(1)
canvas.pack()
print(2)

window.update()
tim = time.time()
while True:
    if NAPRAVLENIE == 0:
        if time.time() - tim > SPEED:
            tim = time.time()
            w(0)
            window.update()
    if NAPRAVLENIE == 1:
        if time.time() - tim > SPEED:
            tim = time.time()
            s(0)
            window.update()
    if NAPRAVLENIE == 2:
        if time.time() - tim > SPEED:
            tim = time.time()
            a(0)
            window.update()
    if NAPRAVLENIE == 3:
        if time.time() - tim > SPEED:
            tim = time.time()
            d(0)
            window.update()








