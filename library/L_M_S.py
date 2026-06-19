from tkinter import*
from tkinter import messagebox
from tkinter import ttk
root=Tk()
root.geometry("544x544")
root.config(bg="lightblue")
root.title("Library-management-system ")
# ================= HOME PAGE =================

def home_page():
    home = Toplevel(root)
    home.title("Library Dashboard")
    home.geometry("900x600")
    home.config(bg="lightblue")

    Label(
        home,
        text="Library Dashboard",
        font=("Arial", 24, "bold"),
        bg="lightblue"
    ).pack(pady=20)

    Button(home, text="Add Book",
           font=("Arial",14,"bold"),
           width=20,
           command=add_book).pack(pady=10)

    Button(home, text="View Books",
           font=("Arial",14,"bold"),
           width=20,command=view_book).pack(pady=10)

    Button(home, text="Issue Book",
           font=("Arial",14,"bold"),
           width=20).pack(pady=10)

    Button(home, text="Return Book",
           font=("Arial",14,"bold"),
           width=20).pack(pady=10)
    Button(home,text="Exit",
           font=("Arial", 14, "bold")
           ,fg="white",bg="red",command=root.destroy).pack(pady=20)
#===============================add book function ========================

def add_book():
    add = Toplevel()
    add.title("Add Book")
    add.geometry("500x400")

    Label(add,text="ADD NEW BOOK",
          fg="blue",
          font=("Arial",20,"bold")).place(x=140,y=10)

    Label(add,text="Book ID:",
          font=("Arial",14,"bold")).place(x=30,y=200)

    id_entry=Entry(add,width=30)
    id_entry.place(x=180,y=200)
    Label(add,text="Book Name:",
          font=("Arial",14,"bold")).place(x=30,y=80)

    book_entry=Entry(add,width=30)
    book_entry.place(x=180,y=80)

    Label(add,text="Author Name:",
          font=("Arial",14,"bold")).place(x=30,y=140)

    author_entry=Entry(add,width=30)
    author_entry.place(x=180,y=140)

    def save_book():
        book = book_entry.get()
        author = author_entry.get()
        book_id = id_entry.get()
        if book=="" or author=="" or book_id=="":
          messagebox.showwarning("warning","Please fill all enteris")
          return
        else:
          with open("books.txt", "a") as file:
            file.write(f"{book_id} |{book} | {author} \n")

        messagebox.showinfo("Success", "Book Saved Successfully")

        

    Button(add,text="Save Book",
           bg="green",
           fg="white", font=("Arial",14,"bold"),command=save_book).place(x=80,y=300,width=100,height=50)

    Button(add,text="Clear",
           bg="orange",
           fg="white", font=("Arial",14,"bold")).place(x=200,y=300,width=100,height=50)

    Button(add,text="Back",
           bg="red",
           fg="white", font=("Arial",14,"bold"),
           command=add.destroy).place(x=350,y=300,width=100,height=50)

def view_book():
    view = Toplevel(root)
    view.title("Books Record")
    view.geometry("800x500")

    tree = ttk.Treeview(
        view,
        columns=("ID","Book", "Author"),
        show="headings"
    )

    tree.heading("ID", text="Book ID")
    tree.heading("Book", text="Book Name")
    tree.heading("Author", text="Author Name")

    tree.column("ID", width=100)
    tree.column("Book", width=250)
    tree.column("Author", width=250)

    tree.pack(fill=BOTH, expand=True)

    try:
        with open("books.txt", "r") as file:
            for line in file:
                data = line.strip().split("|")

                book_id = data[2].replace("Book Id:", "").strip()
                book = data[0].replace("Book:", "").strip()
                author = data[1].replace("Author:", "").strip()

                tree.insert("", END, values=(book_id,book, author))

    except FileNotFoundError:
        messagebox.showerror("Error", "No books found")

#=============================login function=============================
def login():
    if user_Entry.get() =="kamal bhaskar" and pass_Entry.get()=="12345":
        value=messagebox.showinfo("Information","Login Successfully!")
        if value:
            home_page()
            root.withdraw()
    else:
        messagebox.showerror("Error","Invaild Username or Password!")
        return 
Label(root,text="Library Management System ",font="impack 20 bold",bg="lightblue").place(x=100,y=5)
        
img = PhotoImage(file=r"C:\Users\lenovo\Desktop\python\library\book.png")
img = img.subsample(5,5)

label = Label(root, image=img,bg="lightblue")
label.place(x=170,y=80,height=110,width=190)

Label(root,text="Username:",font=("Arial", 14, "bold"),bg="lightblue").place(x=100,y=200)
user_Entry=Entry(root,font=("Arial", 14, "bold"),)
user_Entry.place(x=250,y=200,width=200)

Label(root,text="Password:",font=("Arial", 14, "bold"),bg="lightblue").place(x=100,y=300)
pass_Entry=Entry(root,font=("Arial", 14, "bold"),show="*")
pass_Entry.place(x=250,y=300,width=200)

Button(root,text="login",font=("Arial", 14, "bold"),fg="white",bg="blue",command=login).place(x=100,y=400,width=120,height=50)
Button(root,text="Exit",font=("Arial", 14, "bold"),fg="white",bg="red",command=root.destroy).place(x=250,y=400,width=120,height=50)
Label(root,text="Developed By Kamal Bhaskar",font=("Arial", 10, "italic"),bg="#EAF6F6",fg="gray").pack(side=BOTTOM, pady=10)
#===========================================================================================================================================

root.mainloop()