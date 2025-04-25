import tkinter as tk                           #for GUI
from tkinter import messagebox

# Add credentials to file
def add():
    site = entrySite.get()
    username = entryName.get()
    password = entryPassword.get()

    if site and username and password:
        with open("passwords.txt", 'a') as f:
            f.write(f"{site} {username} {password}\n")
            messagebox.showinfo("Success", f"Password for {site} added!")
    else:
            messagebox.showerror("Error", "Please fill all fields!")

# Get password info by site or username
def get():
    site = entrySite.get()
    username = entryName.get()
    found_entries = []

    try:
        with open("passwords.txt", 'r') as f:
            for line in f:
                data = line.strip().split()
                if len(data) == 3:
                    if (site and data[0] == site) or (username and data[1] == username):
                        found_entries.append(f"Site: {data[0]} | Username: {data[1]} | Password: {data[2]}")

        if found_entries:
            messagebox.showinfo("Password(s) Found", "\n".join(found_entries))
        else:
            messagebox.showinfo("Not Found", "No matching information found.")

    except:
        messagebox.showerror("Error", "Unable to read file!")


def delete():
    site = entrySite.get()
    username = entryName.get()
    updated = []
    found = False

    try:
        with open("passwords.txt", 'r') as f:
            for line in f:
                data = line.strip().split()
                if len(data) == 3:
                    if (site and data[0] == site) or (username and data[1] == username):
                        found = True                 # Do not add to updated (i.e., delete)
                    else:
                        updated.append(line.strip())
                else:
                    updated.append(line.strip())

        with open("passwords.txt", 'w') as f:
            for item in updated:
                f.write(item + "\n")

        if found:
            messagebox.showinfo("Deleted", "Matching entries deleted successfully.")
        else:
            messagebox.showinfo("Not Found", "No matching entry to delete.")

    except Exception as e:
        messagebox.showerror("Error", f"Error: {e}")


# Show all entries
def getlist():
    try:
        with open("passwords.txt", 'r') as f:
            data = f.readlines()

        if not data:
            messagebox.showinfo("List", "No passwords saved yet!")
            return

        msg = "🔐 Saved Passwords:\n"
        for line in data:
            parts = line.strip().split()
            if len(parts) == 3:
                msg += f"Site: {parts[0]} | Username: {parts[1]} | Password: {parts[2]}\n"

        messagebox.showinfo("All Saved Passwords", msg)

    except:
        messagebox.showerror("Error", "Unable to read password file!")

# GUI Setup
if __name__ == "__main__":
    app = tk.Tk()
    app.geometry("400x350")
    app.title("PassKeep")

    # Site input
    tk.Label(app, text="WEBSITE / PLATFORM:").grid(row=0, column=0, padx=10, pady=10)
    entrySite = tk.Entry(app)
    entrySite.grid(row=0, column=1, padx=10, pady=10)

    # Username input
    tk.Label(app, text="USERNAME:").grid(row=1, column=0, padx=10, pady=10)
    entryName = tk.Entry(app)
    entryName.grid(row=1, column=1, padx=10, pady=10)

    # Password input
    tk.Label(app, text="PASSWORD:").grid(row=2, column=0, padx=10, pady=10)
    entryPassword = tk.Entry(app, show="*")
    entryPassword.grid(row=2, column=1, padx=10, pady=10)

  
    # Button to Add a new password
    buttonAdd = tk.Button(app, text="Add", command=add)
    buttonAdd.grid(row=3, column=0, padx=15, pady=10, sticky="we")

    # Button to Get a password for a site
    buttonGet = tk.Button(app, text="Get", command=get)
    buttonGet.grid(row=3, column=1, padx=15, pady=10, sticky="we")

    # Button to List all passwords
    buttonList = tk.Button(app, text="List", command=getlist)
    buttonList.grid(row=4, column=0, padx=15, pady=10, sticky="we")

    # Button to Delete password for a site
    buttonDelete = tk.Button(app, text="Delete", command=delete)
    buttonDelete.grid(row=4, column=1, padx=15, pady=10, sticky="we")

    app.mainloop()
