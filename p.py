"""from tkinter import*
from tkinter import ttk
root = Tk()
root.geometry("600x500")
tree=ttk.Treeview(root)
tree["columns"]=("Roll","name","branch")
tree["show"] = "headings"

tree.heading("Roll",text="roll no")
tree.heading("name",text="Name")
tree.heading("branch",text="Branch")

tree.insert("",END,values=(11,"bhaskar","CSE"))
tree.insert("", END, values=(101, "Kamal", "CSE"))
tree.insert("", END, values=(102, "Amit", "ECE"))
tree.insert("", END, values=(103, "Rahul", "ME"))
tree.insert("", END, values=(104, "Priya", "IT"))
tree.insert("", END, values=(105, "Anjali", "CE"))
tree.insert("", END, values=(106, "Rohan", "EE"))
tree.insert("", END, values=(107, "Sneha", "CSE"))
tree.insert("", END, values=(108, "Vikas", "ME"))
tree.insert("", END, values=(109, "Nehar", "ECE"))
tree.insert("", END, values=(110, "Suresh", "IT"))
def delete_row():
    selected = tree.focus()
    tree.delete(selected)

Button(root,
       text="Delete",
       command=delete_row).pack()
tree.pack()


root.mainloop()"""
from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("600x500")

# Form Frame
frame = Frame(root,bg="green",relief="ridge",borderwidth=12)
frame.grid(row=0,column=1)

Label(frame, text="Roll").grid(row=0, column=0,pady=5)
Label(frame, text="Name").grid(row=1, column=0,pady=5)
Label(frame, text="Branch").grid(row=2, column=0,pady=5,padx=3)

roll_entry = Entry(frame)
name_entry = Entry(frame)
branch_entry = Entry(frame)

roll_entry.grid(row=0, column=1)
name_entry.grid(row=1, column=1)
branch_entry.grid(row=2, column=1)

# Treeview
tree = ttk.Treeview(root)
tree["columns"] = ("Roll", "Name", "Branch")
tree["show"] = "headings"

tree.heading("Roll", text="Roll No")
tree.heading("Name", text="Name")
tree.heading("Branch", text="Branch")

tree.grid(row=0,column=2,padx=10)

# Add Function
def add_student():
    roll = roll_entry.get()
    name = name_entry.get()
    branch = branch_entry.get()

    tree.insert("", END, values=(roll, name, branch))

    # Entry clear
    roll_entry.delete(0, END)
    name_entry.delete(0, END)
    branch_entry.delete(0, END)

# Button
Button(frame,
       text="Add Student",
       command=add_student).grid(row=3, column=1)

root.mainloop()