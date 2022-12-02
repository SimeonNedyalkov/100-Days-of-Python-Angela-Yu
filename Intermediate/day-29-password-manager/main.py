from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list3 = [random.choice(letters) for char in range(nr_letters)]
    password_list1 = [random.choice(symbols) for char in range(nr_symbols)]
    password_list2 = [random.choice(numbers) for char in range(nr_numbers)]
    password_list = password_list2 + password_list1 + password_list3
    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password )
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- Search ------------------------------- #
def find_password():
        website = website_entry.get()
        email = email_entry.get()
        password = password_entry.get()

        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            messagebox.showwarning(title=f"{website}", message="File does not exist")

        else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showwarning(title=f"{website}", message=f"Your email: {email}\nYour password: {password}")
            else:
                messagebox.showwarning(title="NO SUCH WEBSITE", message="You have not registered in this site!!!")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password creator")
window.config(padx=20,pady=20)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=lock_image)

website_label = Label(text="Website:")
website_label.grid(row=2, column=0)

website_entry = Entry(width=20)
website_entry.focus()
website_entry.grid(row=2, column=1, columnspan=1)

search_button = Button(text="Search", command=find_password)
search_button.grid(row=2, column=2)

email_entry = Entry(width=35)
email_entry.insert(0, "simeon_gmail.com")
email_entry.grid(row=3, column=1, columnspan=2)

email_label = Label(text="Email/Username:")
email_label.grid(row=3, column=0)

password_label = Label(text="Password:")
password_label.grid(row=4, column=0)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=4, column=2)

password_entry = Entry(width=21)
password_entry.grid(row=4, column=1)

add_button = Button(text= "add", command= save)
add_button.grid(row=5, column=1)

canvas.grid(row=1, column=1)




canvas.mainloop()
