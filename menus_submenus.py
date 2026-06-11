from tkinter import *

root = Tk()

root.geometry("500x500")
root.title("Menubar")

def new_project():
    print("New Project")

def save():
    print("Save File")

def copy():
    print("Copy Text")

def print_file():
    print("Print File")

def cart():
    print("Added Items")

def exit_app():
    root.destroy()

# Main Menu
mymenu = Menu(root)

# File Menu
filemenu = Menu(mymenu, tearoff=0)

filemenu.add_command(label="New Project", command=new_project)
filemenu.add_command(label="Save", command=save)
filemenu.add_command(label="Copy", command=copy)
filemenu.add_command(label="Print", command=print_file)

# File dropdown attach
mymenu.add_cascade(label="File", menu=filemenu)

# Cart option
mymenu.add_command(label="Cart", command=cart)

# Exit option
mymenu.add_command(label="Exit", command=exit_app)

root.config(menu=mymenu)

root.mainloop()