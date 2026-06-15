from tkinter import *
from tkinter import ttk

root = Tk()

tree = ttk.Treeview(root)

tree["columns"] = (
    "Roll",
    "Name",
    "Branch"
)

tree["show"] = "headings"

tree.heading(
    "Roll",
    text="Roll No"
)

tree.heading(
    "Name",
    text="Name"
)

tree.heading(
    "Branch",
    text="Branch"
)

tree.insert(
    "",
    END,
    values=(101,
            "Kamal",
            "CSE")
)

tree.insert(
    "",
    END,
    values=(102,
            "Rahul",
            "Civil")
)

tree.pack()

root.mainloop()