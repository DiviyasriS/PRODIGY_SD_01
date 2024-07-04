import tkinter as tk
from tkinter import messagebox, simpledialog

contacts = []


def add_contact():
    name = simpledialog.askstring("Input", "Enter Name:")
    phone_number = simpledialog.askstring("Input", "Enter Phone Number:")
    email_address = simpledialog.askstring("Input", "Enter Email Address:")

    if name and phone_number and email_address:
        contacts.append({"name": name, "phone": phone_number, "email": email_address})
        messagebox.showinfo("Success", "Contact added successfully!")
    else:
        messagebox.showerror("Error", "All fields are required!")


def view_contacts():
    contact_window = tk.Tk()
    contact_window.title("Contact List")

    for contact in contacts:
        tk.Label(contact_window, text=f"Name: {contact['name']}").pack()
        tk.Label(contact_window, text=f"Phone: {contact['phone']}").pack()
        tk.Label(contact_window, text=f"Email: {contact['email']}").pack()
        tk.Label(contact_window, text="----------------------------").pack()

    contact_window.mainloop()


def edit_contact():
    view_contacts()
    index = simpledialog.askinteger("Input", "Enter the index of the contact to edit:")

    if 0 <= index < len(contacts):
        name = simpledialog.askstring("Input", "Enter new Name:", initialvalue=contacts[index]['name'])
        phone_number = simpledialog.askstring("Input", "Enter new Phone Number:", initialvalue=contacts[index]['phone'])
        email_address = simpledialog.askstring("Input", "Enter new Email Address:",
                                               initialvalue=contacts[index]['email'])

        if name and phone_number and email_address:
            contacts[index] = {"name": name, "phone": phone_number, "email": email_address}
            messagebox.showinfo("Success", "Contact updated successfully!")
        else:
            messagebox.showerror("Error", "All fields are required!")
    else:
        messagebox.showerror("Error", "Invalid index!")


def delete_contact():
    view_contacts()
    index = simpledialog.askinteger("Input", "Enter the index of the contact to delete:")

    if 0 <= index < len(contacts):
        del contacts[index]
        messagebox.showinfo("Success", "Contact deleted successfully!")
    else:
        messagebox.showerror("Error", "Invalid index!")


def contact_management():
    contact_window = tk.Tk()
    contact_window.title("Contact Management")

    tk.Button(contact_window, text="Add Contact", command=add_contact).pack()
    tk.Button(contact_window, text="View Contacts", command=view_contacts).pack()
    tk.Button(contact_window, text="Edit Contact", command=edit_contact).pack()
    tk.Button(contact_window, text="Delete Contact", command=delete_contact).pack()

    contact_window.mainloop()


if __name__ == "__main__":
    contact_management()
