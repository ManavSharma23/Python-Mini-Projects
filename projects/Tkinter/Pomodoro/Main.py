from tkinter import *

window = Tk()
window.title("Pomodoro")
window.geometry("400x400")
window.config(padx=50,pady=50,bg="#ffc7c7")
canvas = Canvas(width=200,height=224,bg="#ffc7c7",highlightthickness=0)
tomato=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato)
canvas.create_text(100,125,text="00:00",font=("Arial",35,"bold"))
canvas.pack()















window.mainloop()
