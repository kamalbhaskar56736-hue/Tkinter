from tkinter import *
import tkinter.messagebox as tmsg


root = Tk()
root.geometry("500x500")
root.title("kamal Restaurent")

def feedbackrating():
    print("Thank you for choosing our restuarent")
    with open("rating.txt", "a") as f:
        f.write(f"Order was {ordervalue.get()}, bill was {billvalue.get()}, ratings are {slider.get()} points\n")
    tmsg.showinfo("Greetings", "Thank you for choosing our restuarent")


Label(root,text="Welcome to kamal Restaurent").grid(row=0, column=3)

order = Label(root, text="Order").grid(row=1, column=1)
bill = Label(root, text="Pay Bill").grid(row=2, column=1)

ordervalue=StringVar()
billvalue=StringVar()

orderentry = Entry(root, textvariable=ordervalue)
billentry = Entry(root, textvariable=billvalue)

orderentry.grid(row=1, column=2)
billentry.grid(row=2, column=2)


slider = Scale(root, from_=0, to=10, orient=HORIZONTAL)
slider.grid(row=3, column=2)
feedback = Label(text="Some feedback rating").grid(row=4,column=2)

button = Button(root, text="Proceed", command=feedbackrating).grid(row=5, column=2)
root.mainloop()