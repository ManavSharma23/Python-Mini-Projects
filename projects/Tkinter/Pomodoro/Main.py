from tkinter import *

window = Tk()
window.title("Pomodoro")
window.geometry("400x400")

window.config(padx=50, pady=50, bg="#ffc7c7")

# Center column
window.grid_columnconfigure(0, weight=1)

title = Label(text="Timer",
              font=("Times New Roman",40,"bold"),
              fg="black", bg="#ffc7c7")
title.grid(row=0, column=0, pady=10)

canvas = Canvas(width=200, height=224,
                bg="#ffc7c7", highlightthickness=0)

tomato = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato)
canvas.create_text(100,125,text="00:00",
                   font=("Arial",35,"bold"),
                   fill="white")

canvas.grid(row=1, column=0)

start = Button(text="Start",highlightthickness=0,)
start.grid(row=3, column=0,sticky="w")

reset = Button(text="Reset",highlightthickness=0,)
reset.grid(row=3, column=0,sticky="e")

checkmarks=Label(text="✓",highlightthickness=0,bg="#ffc7c7",font=("Aerial",20),fg="green")
checkmarks.grid(row=4, column=0,sticky="s")






window.mainloop()