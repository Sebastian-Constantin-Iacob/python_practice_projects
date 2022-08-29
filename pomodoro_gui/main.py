from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checkmarks = ''
timer = None




# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global reps
    global timer
    global checkmarks

    checkmarks = ''
    timer = window.after_cancel(timer)
    reps = 0
    start_button_clicked()



# ---------------------------- TIMER MECHANISM ------------------------------- #
def count_down(time):
    global reps
    global checkmarks
    global timer

    count_minutes = int(time/60)
    count_seconds = time % 60

    if count_seconds < 10 :
        count_seconds = f'0{count_seconds}'

    if count_minutes < 10:
        count_minutes = f'0{count_minutes}'

    canvas.itemconfig(the_canvas_text, text=f'{count_minutes}:{count_seconds}')
    if time > 0:
        timer = window.after(1000, count_down, time-1)
    else:
        start_button_clicked()
        if (reps % 8 != 0) and (reps % 2 == 0):
            checkmarks += '✔'
            check_label.configure(text=checkmarks)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def start_button_clicked():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        title.configure(text='Long Brake', fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        title.configure(text='Short Brake', fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        title.configure(text='Study', fg=GREEN)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.configure(bg=YELLOW, padx=100, pady=50)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomatoe_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomatoe_img)
the_canvas_text = canvas.create_text(100, 130, font=(FONT_NAME, 35, 'bold'), fill='white', text='00:00')
canvas.grid(column=2, row=2)

title = Label(text='Timer', font=(FONT_NAME, 40, 'normal'), fg=GREEN, bg=YELLOW, highlightthickness=0)
title.grid(column=2, row=1)

start_button = Button(text='Start',bg=YELLOW, highlightthickness=0, command=start_button_clicked)
start_button.grid(column=1, row=3,)

reset_button = Button(text='Reset', bg=YELLOW, highlightthickness=0, command=reset)
reset_button.grid(column=3, row=3)

check_label = Label(font=(FONT_NAME, 20, 'normal'), fg=GREEN, bg=YELLOW, highlightthickness=0)
check_label.grid(column=2, row=4)

window.mainloop()
