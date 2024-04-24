import tkinter
import tkinter.messagebox
import os
import json

def load_users():
    if os.path.exists('users.json'):
        with open('users.json', 'r') as file:
            return json.load(file)
    else:
        return {}

def save_users(users):
    with open('users.json', 'w') as file:
        json.dump(users, file)

def success():
    tkinter.messagebox.showinfo("Login Success", "Welcome, summer!")

def failed():
    tkinter.messagebox.showerror("Login Failed", "Try Again")

def login():
    login_window = tkinter.Tk()
    login_window.title("Login")
    login_window.geometry("300x150")
    
    text_username = tkinter.Entry(login_window)
    text_password = tkinter.Entry(login_window)
    text_username.place(x=80, y=10, width=200, height=25)
    text_password.place(x=80, y=30, width=200, height=25)

    label_username = tkinter.Label(login_window, text="Username")
    label_password = tkinter.Label(login_window, text="Password")
    label_username.place(x=10, y=10)
    label_password.place(x=10, y=30)
    
    tombol_register = tkinter.Button(login_window, text="Register", command=lambda: register(login_window))
    tombol_register.place(x=10, y=90, width=270, height=25)
    
    def on_login_click():
        username = text_username.get()
        password = text_password.get()

        users = load_users()

        if username in users and users[username] == password:
            success()
        else:
            failed()
    
    tombol_login = tkinter.Button(login_window, text="Login", command=on_login_click) 
    tombol_login.place(x=10, y=60, width=270, height=25)
    login_window.mainloop()

def register(login_window):
    register_window = tkinter.Toplevel(login_window)
    register_window.title("Register")
    register_window.geometry("350x120")

    label_username = tkinter.Label(register_window, text="Username")
    label_password = tkinter.Label(register_window, text="Password")
    label_confirm_password = tkinter.Label(register_window, text="Confirm Password")
    label_username.place(x=10, y=10)
    label_password.place(x=10, y=30)
    label_confirm_password.place(x=10, y=50)

    text_username = tkinter.Entry(register_window)
    text_password = tkinter.Entry(register_window, show="*")
    text_confirm_password = tkinter.Entry(register_window, show="*")
    text_username.place(x=130, y=10, width=200, height=25)
    text_password.place(x=130, y=30, width=200, height=25)
    text_confirm_password.place(x=130, y=50, width=200, height=25)

    def on_register_click():
        username = text_username.get()
        password = text_password.get()
        confirm_password = text_confirm_password.get()

        users = load_users()

        if username in users:
            print("Username already exists")
        elif password != confirm_password:
            print("Passwords do not match")
        else:
            users[username] = password
            save_users(users)
            print("User registered successfully")
    register_button = tkinter.Button(register_window, text="Register", command=on_register_click)
    register_button.place(x=10, y=80, width=320, height=25)

login()
