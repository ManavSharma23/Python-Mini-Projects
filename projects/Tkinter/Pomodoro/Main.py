from tkinter import *

#========================Functions=============================================
def start_time():
    count_down(25*60)



def count_down(count):

    min_timer=count//60
    sec_timer=count%60

    canvas.itemconfig(canvas_text, text=f"{min_timer}:{sec_timer}")
    if count > 0:
        window.after(1000, count_down,count-1)

#===============================================================================

#=======================================UI======================================

window = Tk()
window.title("Pomodoro")
window.geometry("400x400")

window.config(padx=50, pady=50, bg="#ffc7c7")

window.grid_columnconfigure(0, weight=1)

title = Label(text="Timer",
              font=("Times New Roman",40,"bold"),
              fg="black", bg="#ffc7c7")
title.grid(row=0, column=0, pady=10)

canvas = Canvas(width=200, height=224,
                bg="#ffc7c7", highlightthickness=0)

tomato = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato)
canvas_text=canvas.create_text(100,125,text="00:00",
                   font=("Arial",35,"bold"),
                   fill="white")

canvas.grid(row=1, column=0)

start = Button(text="Start",highlightthickness=0,command=start_time)
start.grid(row=3, column=0,sticky="w")

reset = Button(text="Reset",highlightthickness=0,)
reset.grid(row=3, column=0,sticky="e")

checkmarks=Label(text="✓",highlightthickness=0,bg="#ffc7c7",font=("Aerial",20),fg="green")
checkmarks.grid(row=4, column=0,sticky="s")

#=====================================================================================



window.mainloop()