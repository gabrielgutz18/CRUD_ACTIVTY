from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector

# Model Class (Now using MySQL database)
class Model:
    def __init__(self):
        self.conn = mysql.connector.connect(
         host="localhost",
         port=3306,  # or use the correct port
         user="root",
         password="200318",
         database="thebestdb"
)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                age INT,
                program VARCHAR(255)
            )
        """)
        self.conn.commit()

    def add_entries(self, name, age, program):
        self.cursor.execute("INSERT INTO students (name, age, program) VALUES (%s, %s, %s)", (name, int(age), program))
        self.conn.commit()

    def edit_entries(self, name, age, program, index):
        self.cursor.execute("UPDATE students SET name = %s, age = %s, program = %s WHERE id = %s", (name, int(age), program, index))
        self.conn.commit()

    def delete_entries(self, index):
        self.cursor.execute("DELETE FROM students WHERE id = %s", (index,))
        self.conn.commit()

    def get_entries(self):
        self.cursor.execute("SELECT * FROM students")
        return self.cursor.fetchall()

# Controller Class
class Controller:
    def __init__(self, view):
        self.view = view
        self.model = Model()
        self.editing_index = None

        self.view.set_submit_button_command(self.submit)
        self.view.set_edit_button_command(self.edit)
        self.view.set_delete_button_command(self.delete)

        self.view.update_listbox(self.model.get_entries())

    def submit(self):
        full_name, age, program = self.view.get_entry_data()
        if not full_name or not age or not program:
            messagebox.showerror("Error", "Please fill in all fields")
            return

        if not age.isdigit():
            messagebox.showerror("Error", "Age must be a number")
            return

        if self.editing_index is None:
            self.model.add_entries(full_name, age, program)
        else:
            self.model.edit_entries(full_name, age, program, self.editing_index)
            self.editing_index = None

        self.view.update_listbox(self.model.get_entries())
        self.view.clear_entries()

    def edit(self):
        selected_item = self.view.treeview.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select an item to edit")
            return

        selected_index = self.view.treeview.index(selected_item)
        entries = self.model.get_entries()
        selected_entry = entries[selected_index]
        name, age, program = selected_entry[1], selected_entry[2], selected_entry[3]

        self.view.set_entry_data(name, age, program)
        self.editing_index = selected_entry[0]

    def delete(self):
        selected_item = self.view.treeview.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select an item to delete")
            return

        selected_index = self.view.treeview.index(selected_item)
        entries = self.model.get_entries()
        self.model.delete_entries(entries[selected_index][0])
        self.view.update_listbox(self.model.get_entries())

# View Class
class View:
    def __init__(self, window):
        window.geometry("900x500")
        window.configure(bg="#0C302F")
        self.window = window

        # Title
        self.title_label = Label(window, text="BSCPE 3A Student Management", bg="#B22222", fg="#FFFFFF", font=("fixedsys", 24, "bold"))
        self.title_label.pack(fill="x")

        # Input fields
        self.full_name_label = Label(window, text="Full Name:", bg="#0C302F", fg="#FFFFFF", font=("Inter", 10))
        self.full_name_label.place(x=730, y=100)
        self.full_name_entry = Entry(window, bg="#FFFFFF", fg="#000000", font=("Inter", 10))
        self.full_name_entry.place(x=733, y=125, width=120, height=20)

        self.age_label = Label(window, text="Age:", bg="#0C302F", fg="#FFFFFF", font=("Inter", 10))
        self.age_label.place(x=730, y=150)
        self.age_entry = Entry(window, bg="#FFFFFF", fg="#000000", font=("Inter", 10))
        self.age_entry.place(x=733, y=175, width=120, height=20)

        self.program_label = Label(window, text="Program:", bg="#0C302F", fg="#FFFFFF", font=("Inter", 10))
        self.program_label.place(x=730, y=200)
        self.program_entry = Entry(window, bg="#FFFFFF", fg="#000000", font=("Inter", 10))
        self.program_entry.place(x=733, y=225, width=120, height=20)

        # Buttons
        self.submit_button = Button(window, text="SUBMIT", command=None, bg="#B22222", fg="#FFFFFF", font=("Inter", 12, "bold"))
        self.submit_button.place(x=733, y=300, width=120, height=30)

        self.edit_button = Button(window, text="UPDATE", command=None, bg="#FFD700", fg="#FFFFFF", font=("Inter", 12, "bold"))
        self.edit_button.place(x=733, y=340, width=120, height=30)

        self.delete_button = Button(window, text="DELETE", command=None, bg="#8B0000", fg="#FFFFFF", font=("Inter", 12, "bold"))
        self.delete_button.place(x=733, y=380, width=120, height=30)

        # Treeview
        self.treeview_frame = Frame(window)
        self.treeview_frame.place(x=20, y=100, width=650, height=350)

        self.treeview = ttk.Treeview(self.treeview_frame, columns=("Name", "Age", "Program"), show="headings")
        self.treeview.heading("Name", text="Name")
        self.treeview.heading("Age", text="Age")
        self.treeview.heading("Program", text="Program")

        self.treeview.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        self.scrollbar = Scrollbar(self.treeview_frame, command=self.treeview.yview)
        self.scrollbar.pack(side="right", fill="y", padx=5, pady=5)
        self.treeview.config(yscrollcommand=self.scrollbar.set)

        window.resizable(True, True)

    def set_submit_button_command(self, command):
        self.submit_button.config(command=command)

    def set_edit_button_command(self, command):
        self.edit_button.config(command=command)

    def set_delete_button_command(self, command):
        self.delete_button.config(command=command)

    def update_listbox(self, entries):
        for row in self.treeview.get_children():
            self.treeview.delete(row)
        for entry in entries:
            self.treeview.insert("", "end", values=entry[1:])

    def get_entry_data(self):
        return self.full_name_entry.get(), self.age_entry.get(), self.program_entry.get()

    def set_entry_data(self, name, age, program):
        self.full_name_entry.delete(0, "end")
        self.full_name_entry.insert(0, name)
        self.age_entry.delete(0, "end")
        self.age_entry.insert(0, age)
        self.program_entry.delete(0, "end")
        self.program_entry.insert(0, program)

    def clear_entries(self):
        self.full_name_entry.delete(0, "end")
        self.age_entry.delete(0, "end")
        self.program_entry.delete(0, "end")

# Main Application
if __name__ == "__main__":
    root = Tk()
    root.title("TEAM BULADO")
    view = View(root)
    controller = Controller(view)
    root.mainloop()
