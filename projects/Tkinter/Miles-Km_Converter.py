import tkinter as tk

# Conversion function
def convert():
    try:
        value = float(entry.get())
        if mode.get() == 1:  # KM → Miles
            result = value * 0.621371
            result_label.config(text=f"{value} km = {result:.4f} miles")
        else:  # Miles → KM
            result = value / 0.621371
            result_label.config(text=f"{value} miles = {result:.4f} km")
    except:
        result_label.config(text="Enter a valid number")

# Window
window = tk.Tk()
window.title("KM ↔ Miles Converter")
window.geometry("350x250")
window.config(bg="#1e1e1e")  # dark background

# Title
title = tk.Label(window, text="KM ↔ Miles Converter",
                 font=("Arial", 14, "bold"),
                 bg="#1e1e1e", fg="white")
title.pack(pady=10)

# Entry
entry = tk.Entry(window, font=("Arial", 12), justify="center")
entry.pack(pady=10)

# Mode (radio buttons)
mode = tk.IntVar(value=1)

frame = tk.Frame(window, bg="#1e1e1e")
frame.pack()

rb1 = tk.Radiobutton(frame, text="KM → Miles",
                     variable=mode, value=1,
                     bg="#1e1e1e", fg="white",
                     selectcolor="#333")
rb1.grid(row=0, column=0, padx=10)

rb2 = tk.Radiobutton(frame, text="Miles → KM",
                     variable=mode, value=2,
                     bg="#1e1e1e", fg="white",
                     selectcolor="#333")
rb2.grid(row=0, column=1, padx=10)

# Button
btn = tk.Button(window, text="Convert",
                font=("Arial", 11, "bold"),
                command=convert)
btn.pack(pady=10)

# Result
result_label = tk.Label(window, text="",
                        font=("Arial", 11),
                        bg="#1e1e1e", fg="white")
result_label.pack(pady=10)

# Run
window.mainloop()