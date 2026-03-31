from tkinter import *

#++++++++++++++++++++++++++Functions+++++++++++++++++++++++

def save():

    website=website_entry.get()
    email_username=Email_username_entry.get()
    password=password_entry.get()

    data_file =  open("Data.txt", "a")
    data_file.write(f"{website} | {email_username} | {password}\n")
    website_entry.delete(0, END)
    Email_username_entry.delete(0, END)
    password_entry.delete(0, END)
    















#+++++++++++++++++++++UI+++++++++++++++++++++++++
window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=50)
canvas=Canvas(width=200,height=200 )
lock_image=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=lock_image)
canvas.grid(row=0,column=1)

website_label=Label(text="Website")
Email_username_label=Label(text="Email/Username")
password_label=Label(text="Password")

website_entry=Entry(width=35)
Email_username_entry=Entry(width=35)
password_entry=Entry(width=20)

password_button=Button(text="Generate Password")
password_button.grid(row=3,column=2)

add_button=Button(text="Add",width=36,command=save)
add_button.grid(row=4,column=1,columnspan=2)

website_label.grid(row=1,column=0)
Email_username_label.grid(row=2,column=0)
password_label.grid(row=3,column=0)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()
Email_username_entry.grid(row=2,column=1,columnspan=2)
password_entry.grid(row=3,column=1)




window.mainloop()