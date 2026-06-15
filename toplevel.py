from tkinter import *

root = Tk()
root.geometry("500x500")

def dashboard():

    top = Toplevel(root)
    top.title("Dashboard")
    top.geometry("700x700")

    Label(top,text="Welcome Kamal").pack()

    def quit():
     top.destroy()
    Button(top,text="exit this window",command=quit).pack()

Button(
    root,
    text="Login",
    command=dashboard
).pack()

root.mainloop()