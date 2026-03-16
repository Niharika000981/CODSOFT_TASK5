import tkinter as tk
from tkinter import messagebox

contacts = []

# ---------- FUNCTIONS ---------- #

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name == "" or phone == "":
        messagebox.showwarning("Warning", "Name and Phone required")
        return

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    update_list()
    clear_fields()


def update_list():
    contact_list.delete(0, tk.END)
    for c in contacts:
        contact_list.insert(tk.END, f"{c['name']} - {c['phone']}")


def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)


def view_contact():
    selected = contact_list.curselection()

    if not selected:
        return

    index = selected[0]
    c = contacts[index]

    name_entry.delete(0, tk.END)
    name_entry.insert(0, c["name"])

    phone_entry.delete(0, tk.END)
    phone_entry.insert(0, c["phone"])

    email_entry.delete(0, tk.END)
    email_entry.insert(0, c["email"])

    address_entry.delete(0, tk.END)
    address_entry.insert(0, c["address"])


def delete_contact():
    selected = contact_list.curselection()

    if not selected:
        return

    contacts.pop(selected[0])
    update_list()
    clear_fields()


def update_contact():
    selected = contact_list.curselection()

    if not selected:
        messagebox.showwarning("Warning", "Select a contact first")
        return

    index = selected[0]

    contacts[index]["name"] = name_entry.get()
    contacts[index]["phone"] = phone_entry.get()
    contacts[index]["email"] = email_entry.get()
    contacts[index]["address"] = address_entry.get()

    update_list()
    clear_fields()


def search_contact():
    keyword = search_entry.get().lower()
    contact_list.delete(0, tk.END)

    for c in contacts:
        if keyword in c["name"].lower() or keyword in c["phone"]:
            contact_list.insert(tk.END, f"{c['name']} - {c['phone']}")


# ---------- UI ---------- #

root = tk.Tk()
root.title("Contact Book")
root.geometry("520x650")
root.configure(bg="#E6E6FA")  # lavender background

# Title
title = tk.Label(
    root,
    text="📒 Contact Book",
    font=("Arial", 24, "bold"),
    bg="#E6E6FA",
    fg="#4B0082"
)
title.pack(pady=15)

# Search section
search_frame = tk.Frame(root, bg="#E6E6FA")
search_frame.pack()

search_entry = tk.Entry(search_frame, width=30, bg="#F3E8FF")
search_entry.pack(side=tk.LEFT, padx=5)

search_btn = tk.Button(
    search_frame,
    text="Search",
    bg="#C8A2C8",
    fg="black",
    command=search_contact
)
search_btn.pack(side=tk.LEFT)

# Contact list
contact_list = tk.Listbox(
    root,
    width=50,
    height=10,
    bg="#F8F4FF"
)
contact_list.pack(pady=15)

view_btn = tk.Button(
    root,
    text="View Selected Contact",
    bg="#C8A2C8",
    command=view_contact
)
view_btn.pack(pady=5)

# Form section
form = tk.Frame(root, bg="#E6E6FA")
form.pack(pady=15)

# Name
tk.Label(form, text="👤 Name", bg="#E6E6FA", font=("Arial",10,"bold")).grid(row=0, column=0, sticky="w")
name_entry = tk.Entry(form, width=35, bg="#F3E8FF")
name_entry.grid(row=1, column=0, pady=5)

# Phone
tk.Label(form, text="📞 Phone", bg="#E6E6FA", font=("Arial",10,"bold")).grid(row=2, column=0, sticky="w")
phone_entry = tk.Entry(form, width=35, bg="#F3E8FF")
phone_entry.grid(row=3, column=0, pady=5)

# Email
tk.Label(form, text="✉️ Email", bg="#E6E6FA", font=("Arial",10,"bold")).grid(row=4, column=0, sticky="w")
email_entry = tk.Entry(form, width=35, bg="#F3E8FF")
email_entry.grid(row=5, column=0, pady=5)

# Address
tk.Label(form, text="📍 Address", bg="#E6E6FA", font=("Arial",10,"bold")).grid(row=6, column=0, sticky="w")
address_entry = tk.Entry(form, width=35, bg="#F3E8FF")
address_entry.grid(row=7, column=0, pady=5)

# Buttons
btn_frame = tk.Frame(root, bg="#E6E6FA")
btn_frame.pack(pady=20)

add_btn = tk.Button(btn_frame, text="Add", bg="#B4E2B4", width=10, command=add_contact)
add_btn.grid(row=0, column=0, padx=10)

update_btn = tk.Button(btn_frame, text="Update", bg="#A7C7E7", width=10, command=update_contact)
update_btn.grid(row=0, column=1, padx=10)

delete_btn = tk.Button(btn_frame, text="Delete", bg="#FF7F7F", width=10, command=delete_contact)
delete_btn.grid(row=1, column=0, pady=10)

clear_btn = tk.Button(btn_frame, text="Clear", bg="#D3D3D3", width=10, command=clear_fields)
clear_btn.grid(row=1, column=1)

root.mainloop()