from tkinter import*
from tkinter import ttk
root =Tk()

text =Text(root,height=10,width=40)
text.pack()

ttk.Button(
    root,
    text="Click"
).pack()


combo = ttk.Combobox(
    root,
    values=[
        "Civil",
        "Mechanical",
        "CSE"
    ]
)

combo.pack()
root.mainloop()