from tkinter import*
from tkinter import messagebox

root = Tk()
root.geometry("600x500")
def new_project():
    ans =messagebox.showinfo("add new project ","you are sure to add project github!")
    print(ans)

def save():
    messagebox.askyesno("confrim","you are sure to save data!")

def copy():
    messagebox.showerror("copy warning","not allow the copy of that data!")

mymenu = Menu(root)
filemenu = Menu(mymenu, tearoff=0)

filemenu.add_command(label="New Project", command=new_project)
filemenu.add_command(label="Save", command=save)
filemenu.add_command(label="Copy", command=copy)

mymenu.add_cascade(label="File", menu=filemenu)
root.config(menu=mymenu)

#login form
Label(root, text="Username").grid(row=0, column=0)

user = Entry(root)
user.grid(row=0, column=1)

def login():
    if user.get() == "":
        messagebox.showerror(
            "Error",
            "Username cannot be empty!"
        )
    else:
        messagebox.showinfo(
            "Success",
            "Login Successful!"
        )

Button(root, text="Login", command=login).grid(row=1, column=1)

root.mainloop()