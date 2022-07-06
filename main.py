from tkinter import *

BROWN = '#9C661F'
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
WORK_MIN = 50
COFFEE_BREAK_MIN = 5
LUNCH_BREAK_MIN = 60
timer = None
hours = 0
check = ""


def reset():
    global hours
    global check
    screen.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    timer_label.config(fg=GREEN)
    check = ""
    check_hours.config(text=check)
    hours = 0



def start_timer():
    global hours
    global check
    work_time = WORK_MIN * 60
    coffee_time = COFFEE_BREAK_MIN * 60
    lunch_time = LUNCH_BREAK_MIN * 60
    hours += 1
    if hours % 8 == 0:
        count_time(lunch_time)
        timer_label.config(text="LUNCH TIME")
        timer_label.config(fg=RED)
        check += "✔"
        check_hours.config(text=check)
    elif hours == 7 or hours == 15:
        count_time(work_time + coffee_time)
        timer_label.config(text="WORK TIME")
        timer_label.config(fg=GREEN)
    elif hours % 2 == 0:
        count_time(coffee_time)
        timer_label.config(text="COFFEE TIME")
        timer_label.config(fg=BROWN)
        check += "✔"
        check_hours.config(text=check)
    else:
        count_time(work_time)
        timer_label.config(text="WORK TIME")
        timer_label.config(fg=GREEN)


def count_time(count):
    global timer
    global hours
    minutes = count // 60
    if minutes < 10:
        minutes = f"0{minutes}"
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        timer = screen.after(1000, count_time, count - 1)
    else:
        start_timer()

    if len(check) == 8:
        timer_label.config(text="TIME GO HOME")
        timer_label.config(fg=GREEN)
        screen.after_cancel(timer)
        canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")


screen = Tk()
screen.title("Work Day Timer")
screen.minsize(300, 300)
screen.config(padx=50, pady=50, bg=YELLOW)

canvas = Canvas(width=380, height=380, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="images.png")
canvas.create_image(190, 190, image=image)
timer_text = canvas.create_text(200, 200, text="00:00", fill="green", font=("Courier", 30, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, highlightthickness=0, font=("Courier", 35, "bold"))
timer_label.grid(column=1, row=0)

check_hours = Label(text=check, fg=GREEN, bg=YELLOW, highlightthickness=0, font=("Courier", 15, "bold"))
check_hours.grid(column=1, row=2)

start_button = Button(text="START", command=start_timer, font=("Courier", 10, "bold"))
start_button.grid(column=0, row=2)

reset_button = Button(text="RESET", command=reset, font=("Courier", 10, "bold"))
reset_button.grid(column=2, row=2)

screen.mainloop()
