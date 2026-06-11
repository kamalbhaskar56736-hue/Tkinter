from tkinter import*
root = Tk()

root.geometry("500x500")
root.title("Newspaper today")
heading = Label(root,text="THE TIMES OF INDIA ",font="40")
date = Label(root,text="09/06/2026",font=("Arial", 14, "underline"))
canvas = Canvas(root, width=200, height=60)
canvas.pack()

y = 30
canvas.create_line(0, y, 700, y)
heading.pack()
date.pack()
root.mainloop()