from tkinter import *

root = Tk()

root.geometry("655x355")

Label(root, text="Give your details carefully!", font=("Arial", 16)).grid(row=0, column=1, pady=5)

Label(root, text="Name:").grid(row=1, column=1)
Label(root, text="Phone Number:").grid(row=2, column=1)
Label(root, text="Gender:").grid(row=3, column=1)
Label(root, text="Emergency Number:").grid(row=4, column=1)
Label(root, text="Payment Mode:").grid(row=5, column=1)

userentry = Entry(root)
userentry.grid(row=1, column=2)

phoneentry = Entry(root)
phoneentry.grid(row=2, column=2)

genderentry = Entry(root)
genderentry.grid(row=3, column=2)

emergencyentry = Entry(root)
emergencyentry.grid(row=4, column=2)

paymententry = Entry(root)
paymententry.grid(row=5, column=2)

# Checkbox variable
foodservice = IntVar()

# Checkbox
Checkbutton(
    root,
    text="Want food service?",
    variable=foodservice
).grid(row=6, column=2, pady=5)

# Button function
def submit():
    print("Name:", userentry.get())
    print("Phone:", phoneentry.get())
    print("Gender:", genderentry.get())
    print("Emergency:", emergencyentry.get())
    print("Payment Mode:", paymententry.get())

    if foodservice.get() == 1:
        print("Food Service: Yes")
    else:
        print("Food Service: No")

# Submit Button
Button(root, text="Submit", command=submit).grid(row=7, column=2, pady=10)

root.mainloop()