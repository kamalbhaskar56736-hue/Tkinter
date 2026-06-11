from tkinter import*

root = Tk()

root.title("List box")
root.geometry("700x500")

listbox = Listbox(root)
listbox.pack()

listbox.insert(END, "Pizza")
listbox.insert(END, "Burger")
listbox.insert(END, "Pasta")

def Show():
    selected = listbox.get(listbox.curselection()) #listbox.curselection()=Selected item ka index deta hai.
    print(selected)

Button(root,
       text="Show",
       command=Show).pack()

lb = Listbox(root,
             selectmode=MULTIPLE)

lb.pack()

lb.insert(END, "Python")
lb.insert(END, "Java")
lb.insert(END, "C")
lb.insert(END, "C++")

def show():
    for i in lb.curselection():
        print(lb.get(i))

Button(root,
       text="Show",
       command=show).pack()

root.mainloop()