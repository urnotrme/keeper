from tkinter import *
from random import randrange

win = Tk()
win.title("Keeper")
win.geometry("700x600+410+100")
win.config(bg="pink")

canvas = Canvas(width=700, height=600, bg="pink")
canvas.pack()

canvas.create_rectangle(0, 500, 700, 600, fill="palevioletred", width=0)

k_speed = 0
keeper = canvas.create_rectangle(0, 500, 50, 515, fill="white", width=0)

ball = canvas.create_oval(30, 50, 60, 80, fill="linen", width=0)

count = 0
tc = canvas.create_text(625, 560, text="Count: 0", font="Georgia 18")

b_speed = 4
def move_ball():
    global count
    global game_flag
    global b_speed

    canvas.move(ball, 0, b_speed)

    if canvas.coords(ball)[3] >=500:
        x_ball = canvas.coords(ball)[0] + 15
        if canvas.coords(keeper)[0] < x_ball < canvas.coords(keeper)[2]:
            count += 1
            canvas.itemconfig(tc, text="Count: " + str(count))
            x_random = randrange(20, 680)
            canvas.coords(ball, x_random, 0, x_random+30, 30)
            #b_speed += 1 #по желанию
        else:
            game_flag = False


def move_keeper():
    if (k_speed > 0 and canvas.coords(keeper)[2] < 700) or \
            (k_speed < 0 and canvas.coords(keeper)[0] > 0):
        canvas.move(keeper, k_speed, 0)


game_flag = True
def main():
    move_ball()
    move_keeper()
    if game_flag: # игра продолжается
        win.after(30, main)
    else: # игра окончена
        canvas.create_text(350, 250, text="Game over", font="Georgia 26")

def key_all(event):
    global k_speed

    if event.keysym == "Left":
        k_speed = -5
    elif event.keysym == "Right":
        k_speed = 5
    elif event.keysym == "space":
        k_speed = 0


win.bind("<KeyPress>", key_all)

# вызов главной функции игры
main()

win.mainloop()