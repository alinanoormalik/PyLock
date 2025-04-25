import tkinter as tk                            #for GUI
from tkinter import messagebox
import re                                       # for regular expressions


# Define a function to check password strength
def check_password_strength(user_password):
    # Start with a score of 0
    score = 0

    # Check the length of the password
    if len(user_password) >= 8:
        score += 1  

    # Check for lowercase letters
    if re.search(r"[a-z]", user_password):
        score += 1  

    # Check for uppercase letters
    if re.search(r"[A-Z]", user_password):
        score += 1 

    # Check for numbers
    if re.search(r"[0-9]", user_password):
        score += 1

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", user_password):
        score += 1 

    # Give feedback based on the score
    if score == 5:
        return "Password is strong 💪"
    elif score >= 3:
        return "Password is moderate 😐"
    else:
        return "Password is weak ⚠️"

def check_Password():
    user_password = entryPassword.get()
    result=check_password_strength(user_password)
    messagebox.showinfo("Password Strength:",result)

if __name__ == "__main__":
    app = tk.Tk()
    app.geometry("350x100")
    app.title("PassShield")
    
     # Label and Entry
    tk.Label(app, text="Enter your password:").grid(row=0, column=0, padx=5, pady=10)
    entryPassword = tk.Entry(app, show="*", width=30)
    entryPassword.grid(row=0, column=1, padx=5, pady=5)

    # Button to check password
    buttonCheck = tk.Button(app, text="Check Strength", command=check_Password)
    buttonCheck.grid(row=1, column=0, columnspan=2, pady=10)

    app.mainloop()
