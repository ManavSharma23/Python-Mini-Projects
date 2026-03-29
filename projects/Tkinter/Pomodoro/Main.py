from tkinter import *

# ===================== Variables =====================
no_of_checkmarks = 0
work_time = 30
short_break_time = 5
long_break_time = 10
timer = None

# ===================== Functions =====================

def start_time():
    global no_of_checkmarks
    no_of_checkmarks += 1

    work_sec = int(work_time * 60)
    short_break_sec = int(short_break_time * 60)
    long_break_sec = int(long_break_time * 60)

    if no_of_checkmarks % 8 == 0:
        count_down(long_break_sec)
        title.config(text="Long Break", fg="red")

    elif no_of_checkmarks % 2 == 0:
        count_down(short_break_sec)
        title.config(text="Short Break", fg="blue")

    else:
        count_down(work_sec)
        title.config(text="Work", fg="green")


def count_down(count):
    global timer

    min_timer = count // 60
    sec_timer = count % 60

    canvas.itemconfig(canvas_text, text=f"{min_timer:02d}:{sec_timer:02d}")

    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_time()

        # Update checkmarks
        marks = ""
        work_session = no_of_checkmarks // 2
        for _ in range(work_session):
            marks += "✔"
        checkmarks.config(text=marks)


def reset_button():
    global no_of_checkmarks, timer

    if timer is not None:
        window.after_cancel(timer)

    no_of_checkmarks = 0

    # Reset UI
    canvas.itemconfig(canvas_text, text="00:00")
    title.config(text="Timer", fg="black")
    checkmarks.config(text="")

# ===================== UI =====================

window = Tk()
window.title("Pomodoro")
window.geometry("400x400")
window.config(padx=50, pady=50, bg="#ffc7c7")

window.grid_columnconfigure(0, weight=1)

title = Label(text="Timer",
              font=("Times New Roman", 40, "bold"),
              fg="black", bg="#ffc7c7")
title.grid(row=0, column=0, pady=10)

canvas = Canvas(width=200, height=224,
                bg="#ffc7c7", highlightthickness=0)

tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
canvas_text = canvas.create_text(100, 125, text="00:00",
                                 font=("Arial", 35, "bold"),
                                 fill="white")

canvas.grid(row=1, column=0)

start = Button(text="Start", command=start_time)
start.grid(row=3, column=0, sticky="w")

reset = Button(text="Reset", command=reset_button)
reset.grid(row=3, column=0, sticky="e")

checkmarks = Label(bg="#ffc7c7",
                   font=("Arial", 20),
                   fg="green")
checkmarks.grid(row=4, column=0)

window.mainloop()