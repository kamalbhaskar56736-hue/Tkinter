from tkinter import*
root = Tk()
root.geometry("600x500")

def hello():
    print("hello kamal")

def welcome():
    print("welcome to tkinter")


frame = Frame(root,borderwidth=5,bg="red",relief="solid")
frame.pack(side="left",anchor="ne")

b1 = Button(frame,fg="black",text="print1",command=hello,bg="green")
b1.pack(side="left",padx=20)

b2 = Button(frame,fg="black",text="print2",command=welcome)
b2.pack(side="left",padx=20)

b3 = Button(frame,fg="black",text="print3")
b3.pack(side="left",padx=20)

b4 = Button(frame,fg="black",text="print4")
b4.pack(side="left",padx=20)

b5 = Button(frame,fg="black",text="print5")
b5.pack(side="left",padx=20)
root.mainloop()