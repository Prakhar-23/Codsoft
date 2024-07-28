import tkinter as tk
from tkinter import messagebox

# List to store contact information
contacts = []

class ContactManagerApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Contact Manager")
        self.geometry("400x400")

        self.create_main_menu()

    def create_main_menu(self):
        self.clear_screen()
        tk.Label(self, text="Contact Manager", font=("Helvetica", 16)).pack(pady=10)

        tk.Button(self, text="Add Contact", command=self.add_contact_screen).pack(pady=5)
        tk.Button(self, text="View Contacts", command=self.view_contacts_screen).pack(pady=5)
        tk.Button(self, text="Search Contact", command=self.search_contact_screen).pack(pady=5)
        tk.Button(self, text="Update Contact", command=self.update_contact_screen).pack(pady=5)
        tk.Button(self, text="Delete Contact", command=self.delete_contact_screen).pack(pady=5)
        tk.Button(self, text="Exit", command=self.quit).pack(pady=5)

    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()

    def add_contact_screen(self):
        self.clear_screen()
        tk.Label(self, text="Add Contact", font=("Helvetica", 16)).pack(pady=10)

        tk.Label(self, text="Name:").pack(pady=5)
        self.name_entry = tk.Entry(self)
        self.name_entry.pack(pady=5)

        tk.Label(self, text="Phone Number:").pack(pady=5)
        self.phone_entry = tk.Entry(self)
        self.phone_entry.pack(pady=5)

        tk.Label(self, text="Email:").pack(pady=5)
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(pady=5)

        tk.Label(self, text="Address:").pack(pady=5)
        self.address_entry = tk.Entry(self)
        self.address_entry.pack(pady=5)

        tk.Button(self, text="Save Contact", command=self.save_contact).pack(pady=20)
        tk.Button(self, text="Back", command=self.create_main_menu).pack(pady=5)

    def save_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        contacts.append({'name': name, 'phone': phone, 'email': email, 'address': address})
        messagebox.showinfo("Success", f"Contact {name} added successfully.")
        self.create_main_menu()

    def view_contacts_screen(self):
        self.clear_screen()
        tk.Label(self, text="View Contacts", font=("Helvetica", 16)).pack(pady=10)

        if not contacts:
            tk.Label(self, text="No contacts available.").pack(pady=10)
        else:
            for idx, contact in enumerate(contacts, start=1):
                tk.Label(self, text=f"{idx}. {contact['name']} - {contact['phone']}").pack(pady=2)

        tk.Button(self, text="Back", command=self.create_main_menu).pack(pady=20)

    def search_contact_screen(self):
        self.clear_screen()
        tk.Label(self, text="Search Contact", font=("Helvetica", 16)).pack(pady=10)

        tk.Label(self, text="Enter name or phone number:").pack(pady=5)
        self.search_entry = tk.Entry(self)
        self.search_entry.pack(pady=5)

        tk.Button(self, text="Search", command=self.perform_search).pack(pady=10)
        tk.Button(self, text="Back", command=self.create_main_menu).pack(pady=5)

    def perform_search(self):
        search_term = self.search_entry.get()
        found_contacts = [contact for contact in contacts if search_term in contact['name'] or search_term in contact['phone']]

        self.clear_screen()
        tk.Label(self, text="Search Results", font=("Helvetica", 16)).pack(pady=10)

        if found_contacts:
            for contact in found_contacts:
                tk.Label(self, text=f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}").pack(pady=2)
        else:
            tk.Label(self, text="No contacts found.").pack(pady=10)

        tk.Button(self, text="Back", command=self.create_main_menu).pack(pady=20)

    def update_contact_screen(self):
        self.clear_screen()
        tk.Label(self, text="Update Contact", font=("Helvetica", 16)).pack(pady=10)

        tk.Label(self, text="Enter name or phone number to update:").pack(pady=5)
        self.update_search_entry = tk.Entry(self)
        self.update_search_entry.pack(pady=5)

        tk.Button(self, text="Search", command=self.perform_update_search).pack(pady=10)
        tk.Button(self, text="Back", command=self.create_main_menu).pack(pady=5)

    def perform_update_search(self):
        search_term = self.update_search_entry.get()
        for contact in contacts:
            if search_term in contact['name'] or search_term in contact['phone']:
                self.clear_screen()
                tk.Label(self, text="Update Contact", font=("Helvetica", 16)).pack(pady=10)

                tk.Label(self, text=f"Current Name: {contact['name']}").pack(pady=2)
                self.new_name_entry = tk.Entry(self)
                self.new_name_entry.pack(pady=2)

                tk.Label(self, text=f"Current Phone: {contact['phone']}").pack(pady=2)
                self.new_phone_entry = tk.Entry(self)
                self.new_phone_entry.pack(pady=2)

                tk.Label(self, text=f"Current Email: {contact['email']}").pack(pady=2)
                self.new_email_entry = tk.Entry(self)
                self.new_email_entry.pack(pady=2)

                tk.Label(self, text=f"Current Address: {contact['address']}").pack(pady=2)
                self.new_address_entry = tk.Entry(self)
                self.new_address_entry.pack(pady=2)

                tk.Button(self, text="Save Changes", command=lambda: self.save_update(contact)).pack(pady=10)
                tk.Button(self, text="Back", command=self.create_main_menu).pack(pady=5)
                return
        
        tk.Label(self, text="Contact not found.").pack(pady=10)

    def save_update(self, contact):
        contact['name'] = self.new_name_entry.get() or contact['name']
        contact['phone'] = self.new_phone_entry.get() or contact['phone']
        contact['email'] = self.new_email_entry.get() or contact['email']
        contact['address'] = self.new_address_entry.get() or contact['address']
        messagebox.showinfo("Success", "Contact updated successfully.")
        self.create_main_menu()

    def delete_contact_screen(self):
        self.clear_screen()
        tk.Label(self, text="Delete Contact", font=("Helvetica", 16)).pack(pady=10)

        tk.Label(self, text="Enter name or phone number to delete:").pack(pady=5)
        self.delete_entry = tk.Entry(self)
        self.delete_entry.pack(pady=5)

        tk.Button(self, text="Delete", command=self.perform_delete).pack(pady=10)
        tk.Button(self, text="Back", command=self.create_main_menu).pack(pady=5)

    def perform_delete(self):
        delete_term = self.delete_entry.get()
        for contact in contacts:
            if delete_term in contact['name'] or delete_term in contact['phone']:
                contacts.remove(contact)
                messagebox.showinfo("Success", f"Contact {contact['name']} deleted successfully.")
                self.create_main_menu()
                return
        
        tk.Label(self, text="Contact not found.").pack(pady=10)

if __name__ == "__main__":
    app = ContactManagerApp()
    app.mainloop()
