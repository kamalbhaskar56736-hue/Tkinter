from tkinter import*
from tkinter import messagebox

root = Tk()
root.geometry("655x400")
root.title("Radio button")

def order():
    messagebox.showinfo("order Recived!",f"we have Recived your order for {var.get()}. Thanks for ordering")

var =StringVar()
var.set("Radio")
Label(root,text="what would you like to have sir",font=19,justify=LEFT,padx=14).pack()

radio=Radiobutton(root,text="Dosa",padx=14,variable=var,value="Dosa").pack(anchor="w")
radio=Radiobutton(root,text="Idly",padx=14,variable=var,value="Idly").pack(anchor="w")
radio=Radiobutton(root,text="Due",padx=14,variable=var,value="Due").pack(anchor="w")
radio=Radiobutton(root,text="samosa",padx=14,variable=var,value="samosa").pack(anchor="w")

Button(text="order now",command=order).pack(anchor="w")

gender = StringVar()
gender.set("Male")   # Default value

Radiobutton(root,
            text="Male",
            variable=gender,
            value="Male").pack(anchor="w")

Radiobutton(root,
            text="Female",
            variable=gender,
            value="Female").pack(anchor="w")

Radiobutton(root,
            text="Other",
            variable=gender,
            value="Other").pack(anchor="w")

def show():
    print(gender.get())

Button(root,
       text="Submit",
       command=show).pack(anchor="w")

           
root.mainloop()