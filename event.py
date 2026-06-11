from tkinter import *

root = Tk()
root.geometry("666x600")

def hello():
    Label(root,text="Button Clicked").pack()

btn = Button(root, text="Click Me", command=hello)
btn.pack()
#Mouse Enter and Leave

label = Label(root, text="Hover Over Me")
label.pack()

def enter(event):
    print("Mouse Enter")

def leave(event):
    print("Mouse Leave")

label.bind("<Enter>", enter)
label.bind("<Leave>", leave)

#Keyboard Event
def key_press(event):
    print(event.keysym)

root.bind("<Key>", key_press)

root.mainloop()