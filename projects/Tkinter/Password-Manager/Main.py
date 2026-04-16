from tkinter import *
from tkinter import messagebox
import random
import json

# -------------------- DATA --------------------
letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("0123456789")
signs = ['!', '@', '#', '$', '%', '&', '*', '(', ')']


# -------------------- FUNCTIONS --------------------
def generate_password():
    password = []

    # Random lengths
    letter_length = random.randint(4, 8)
    number_length = random.randint(2, 4)
    sign_length = random.randint(2, 4)

    for _ in range(letter_length):
        password.append(random.choice(letters))

    for _ in range(number_length):
        password.append(random.choice(numbers))

    for _ in range(sign_length):
        password.append(random.choice(signs))

    random.shuffle(password)

    generated_password = ''.join(password)

    password_entry.delete(0, END)
    password_entry.insert(0, generated_password)


def save():
    website = website_entry.get()
    email_username = Email_username_entry.get()
    password = password_entry.get()

    new_data={
        website:{
            "email":email_username,
            "password":password
        }
    }

    if len(website) == 0 or len(email_username) == 0 or len(password) == 0:
        messagebox.showerror("Error", "Please fill all fields")
    else:
        try:
            with open("Data.json", "r") as file:
                data=json.load(file)
        except FileNotFoundError:
            with open("Data.json", "w") as file:
                json.dump(new_data, file,indent=4)
        else:
            data.update(new_data)

        with open("Data.json", "w") as file:
            json.dump(data, file, indent=4)

        messagebox.showinfo("Success", "Your details saved")

        website_entry.delete(0, END)
        password_entry.delete(0, END)


def search():
    website = website_entry.get()
    try:
        with open("Data.json", "r") as file:
            data=json.load(file)
    except FileNotFoundError:
        messagebox.showerror("Error", "No File Found")
    else:
        if website in data:
            email=data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}, Password: {password}")
        else:
            messagebox.showerror("Error", "No Data Found")
# -------------------- UI --------------------
window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=50)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website")
Email_username_label = Label(text="Email/Username")
password_label = Label(text="Password")

# Entries
website_entry = Entry(width=20)
Email_username_entry = Entry(width=34)
password_entry = Entry(width=20)

website_entry.focus()

# Buttons
password_button = Button(text="Generate Password", command=generate_password)
add_button = Button(text="Add", width=35, command=save)
search_button = Button(text="Search",command=search)

# Layout
website_label.grid(row=1, column=0)
Email_username_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)

website_entry.grid(row=1, column=1, )
Email_username_entry.grid(row=2, column=1, columnspan=2)
password_entry.grid(row=3, column=1)

password_button.grid(row=3, column=2)
add_button.grid(row=4, column=1, columnspan=2)
add_button.config(bg="cyan")
search_button.grid(row=1, column=2)


window.mainloop()
