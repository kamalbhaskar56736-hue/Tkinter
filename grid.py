from tkinter import *

root = Tk()
root.geometry("655x500")


frame = Frame(root, borderwidth=5, bg="green", relief="solid",width=300, height=200)
frame.pack(pady=10)


name = Label(frame, text="Username")
name.grid(row=0, column=0, padx=5, pady=5)

userentry = Entry(frame)
userentry.grid(row=0, column=1, padx=5, pady=5)

password = Label(frame,text="password")
password.grid(row=1,column=0,padx=2,pady=2)

passentry=Entry(frame,show="*")
passentry.grid(row=1, column=1, padx=5, pady=5)

email = Label(frame,text="Email:")
email.grid(row=2,column=0)

emailentry=Entry(frame)
emailentry.grid(row=2,column=1,padx=5,pady=5)

def show_data():
    username = userentry.get()
    pass_value=passentry.get()
    email_value=emailentry.get()

    print(username)
    print(pass_value)
    print(email_value)


b1 = Button(frame, text="Login", command=show_data)
b1.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()