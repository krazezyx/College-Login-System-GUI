import hashlib
import random
import string
import webbrowser
import json
import tkinter as tk
from tkinter import messagebox

# Function to generate a password for the user
def generate_password(length=8, chars=string.ascii_letters + string.digits + string.punctuation):
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

# Function to save the user data to a file
def save_user_data():
    with open("user_data.json", "w") as f:
        json.dump(user_data, f)

# Function to load the user data from a file
def load_user_data():
    global user_data
    try:
        with open("user_data.json", "r") as f:
            user_data = json.load(f)
    except FileNotFoundError:
        user_data = {}

# Initial user data load
user_data = {}
load_user_data()

# GUI for registration and login
def register():
    def save_registration():
        username = entry_username.get()
        password = entry_password.get()
        role = role_var.get()

        if username in user_data:
            messagebox.showerror("Error", "Username already exists!")
        else:
            user_data[username] = {
                "password": hashlib.sha256(password.encode()).hexdigest(),
                "role": role
            }
            save_user_data()
            messagebox.showinfo("Success", "Registration successful!")
            register_window.destroy()

    register_window = tk.Toplevel(main_window)
    register_window.title("Register")
    register_window.geometry("400x300")

    tk.Label(register_window, text="Username:").pack(pady=5)
    entry_username = tk.Entry(register_window, width=30)
    entry_username.pack(pady=5)

    tk.Label(register_window, text="Password:").pack(pady=5)
    entry_password = tk.Entry(register_window, show="*", width=30)
    entry_password.pack(pady=5)

    role_var = tk.StringVar(register_window)
    role_var.set("Student")
    tk.Label(register_window, text="Role:").pack(pady=5)
    tk.OptionMenu(register_window, role_var, "Student", "Teacher", "Admin").pack(pady=5)

    tk.Button(register_window, text="Register", command=save_registration).pack(pady=20)

def login():
    def verify_login():
        username = entry_username.get()
        password = hashlib.sha256(entry_password.get().encode()).hexdigest()

        if username in user_data and user_data[username]["password"] == password:
            messagebox.showinfo("Success", f"Login successful! Welcome {username}")
            login_window.destroy()
            role = user_data[username]["role"]
            open_role_interface(role, username)
        else:
            messagebox.showerror("Error", "Invalid username or password!")

    login_window = tk.Toplevel(main_window)
    login_window.title("Login")
    login_window.geometry("400x200")

    tk.Label(login_window, text="Username:").pack(pady=5)
    entry_username = tk.Entry(login_window, width=30)
    entry_username.pack(pady=5)

    tk.Label(login_window, text="Password:").pack(pady=5)
    entry_password = tk.Entry(login_window, show="*", width=30)
    entry_password.pack(pady=5)

    tk.Button(login_window, text="Login", command=verify_login).pack(pady=20)

def open_role_interface(role, username):
    if role == "Student":
        student_interface(username)
    elif role == "Teacher":
        teacher_interface(username)
    elif role == "Admin":
        admin_interface(username)

def student_interface(username):
    student_window = tk.Toplevel(main_window)
    student_window.title("Student Interface")
    student_window.geometry("400x200")

    tk.Label(student_window, text=f"Welcome, {username}!", font=("Arial", 14)).pack(pady=20)
    tk.Label(student_window, text="Student interface - functionality to be added.").pack(pady=10)

def teacher_interface(username):
    teacher_window = tk.Toplevel(main_window)
    teacher_window.title("Teacher Interface")
    teacher_window.geometry("400x200")

    tk.Label(teacher_window, text=f"Welcome, {username}!", font=("Arial", 14)).pack(pady=20)
    tk.Label(teacher_window, text="Teacher interface - functionality to be added.").pack(pady=10)

def admin_interface(username):
    def view_applications():
        applications_window = tk.Toplevel(main_window)
        applications_window.title("Applications")
        applications_window.geometry("400x300")

        applications = ["Sample Application 1", "Sample Application 2"]  # Placeholder

        for app in applications:
            tk.Label(applications_window, text=app).pack(pady=5)

    admin_window = tk.Toplevel(main_window)
    admin_window.title("Admin Interface")
    admin_window.geometry("400x200")

    tk.Label(admin_window, text=f"Welcome, {username}!", font=("Arial", 14)).pack(pady=20)
    tk.Button(admin_window, text="View Applications", command=view_applications).pack(pady=10)

# GUI to collect student information
def collect_student_info():
    def submit_info():
        first_name = entry_first_name.get()
        last_name = entry_last_name.get()
        parent_email = entry_parent_email.get()

        if not first_name or not last_name or not parent_email:
            messagebox.showerror("Error", "All fields are required!")
            return

        full_name = first_name + " " + last_name
        student_email = full_name.replace(" ", ".").lower() + "@mayfieldschool.net"
        password = generate_password()

        messagebox.showinfo("Info", f"Welcome {full_name} to Mayfield School!\n"
                                    f"This will be your student email address: {student_email}\n"
                                    f"Password: {password}")

        webbrowser.open_new_tab("https://www.mayfieldschool.net")
        webbrowser.open_new_tab("https://outlook.office.com/login")

        # Simulate sending email
        print(f"Sending confirmation email/2 Step verification to: {parent_email}")

        student_info_window.destroy()

    student_info_window = tk.Toplevel(main_window)
    student_info_window.title("Student Information")
    student_info_window.geometry("400x300")

    tk.Label(student_info_window, text="First Name:").pack(pady=5)
    entry_first_name = tk.Entry(student_info_window, width=30)
    entry_first_name.pack(pady=5)

    tk.Label(student_info_window, text="Last Name:").pack(pady=5)
    entry_last_name = tk.Entry(student_info_window, width=30)
    entry_last_name.pack(pady=5)

    tk.Label(student_info_window, text="Parent/Guardian Email:").pack(pady=5)
    entry_parent_email = tk.Entry(student_info_window, width=30)
    entry_parent_email.pack(pady=5)

    tk.Button(student_info_window, text="Submit", command=submit_info).pack(pady=20)

def main_menu():
    global main_window
    main_window = tk.Tk()
    main_window.title("College School Login System")
    main_window.geometry("400x200")

    tk.Label(main_window, text="College School Login System", font=("Arial", 16)).pack(pady=20)
    tk.Button(main_window, text="Register", command=register, width=15).pack(pady=10)
    tk.Button(main_window, text="Login", command=login, width=15).pack(pady=10)
    tk.Button(main_window, text="Collect Student Info", command=collect_student_info, width=20).pack(pady=10)

    main_window.mainloop()

# Run the main menu
main_menu()