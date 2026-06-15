from tkinter import *

root = Tk()
root.geometry("600x500")

statusvar = StringVar()
statusvar.set("Ready")

def upload():
    statusvar.set("Uploading...")
    root.after(3000, finish)

def finish():
    statusvar.set("Upload Complete")

Button(root,
       text="Upload",
       command=upload).pack()

sbar = Label(root,
             textvariable=statusvar,
             relief=SUNKEN,
             anchor=W)

sbar.pack(side=BOTTOM, fill=X)

root.mainloop()