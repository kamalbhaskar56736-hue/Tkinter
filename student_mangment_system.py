from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.geometry("1200x715")
root.title("S.M.S")
root.resizable(False, False)

Label(root,
      text="Student Management System",
      font=("Helvetica", 40),
      fg="red",
      bg="white").pack(fill=X)

f1=LabelFrame(root,text='Student Information',borderwidth=4,font='impack 28 bold',bg="orange",bd=5)
f1.place(x=0,y=65, width=1200, height=200)

#label
Label(f1,text="Name:",font="ariel 12 bold",bg="orange").place(x=30,y=10)
Label(f1,text="Roll no:",font="ariel 12 bold",bg="orange").place(x=30,y=40)
Label(f1,text="Gender:",font="ariel 12 bold",bg="orange").place(x=30,y=70)
Label(f1,text="Father name:",font="ariel 12 bold",bg="orange").place(x=400,y=10)
Label(f1,text="Mobile no:",font="ariel 12 bold",bg="orange").place(x=400,y=40)
Label(f1,text="D.O.B:",font="ariel 12 bold",bg="orange").place(x=400,y=70)
Label(f1,text="Adress:",font="ariel 12 bold",bg="orange").place(x=790,y=40)

#entry
e1=Entry(f1,bd=3,font='impack 10 bold',width=25)
e1.place(x=130,y=10)
e2=Entry(f1,bd=3,font='impack 10 bold',width=25)
e2.place(x=130,y=40)
combo=ttk.Combobox(f1,font='impack 10 bold',width=23)
combo['values']=("Male","Female","other")
combo.place(x=130,y=70)
e4=Entry(f1,bd=3,font='impack 10 bold',width=25)
e4.place(x=530,y=10)
e5=Entry(f1,bd=3,font='impack 10 bold',width=25)
e5.place(x=530,y=40)
e6=Entry(f1,bd=3,font='impack 10 bold',width=25)
e6.place(x=530,y=70)
address_txt=Text(f1,bd=3,font='impack 10 bold')
address_txt.place(x=900,y=2,width=270,height=100)


def search_student():

    roll = search_entry.get()

    for item in table.get_children():

        values = table.item(item)["values"]

        if str(values[1]) == roll:   

            table.selection_set(item)
            table.focus(item)
            table.see(item)

            messagebox.showinfo(
                "Found",
                "Student Found"
            )
            return

    messagebox.showerror(
        "Not Found",
        "Student Not Found"
    )
#frame 1
f2=Frame(root,bg='lightgreen',bd=4)
f2.place(x=0,y=210,width=1200,height=65)

Label(f2,text="Search",bd=3,font='impack 20 bold',bg="lightgreen").place(x=160,y=7)
search_entry=Entry(f2,bd=3,font='impack 20 bold')
search_entry.place(x=300, y=8)
Button(f2,text="Search",font="impack 12 bold",bd=2,bg="yellow",command=search_student).place(x=700,y=7,width=100)



f3=LabelFrame(root,text='Student Data',borderwidth=4,font='impack 18 bold',bg="grey",bd=5)
f3.place(x=0,y=265, width=1200, height=400)

table=ttk.Treeview(f3,columns=('name',"roll no","gender","father name",'d.o.b','contact',"address"))
table["show"] = "headings"
table.heading("name",text="Name")
table.heading("roll no",text="Roll No")
table.heading("gender",text="Gender")
table.heading("father name",text="Father Name")
table.heading("d.o.b",text="D.O.B")
table.heading("contact",text="Contact")
table.heading("address",text="Address")
table.pack(fill="both",expand=1)

#heading columns
table.column("name",width=170)
table.column("roll no",width=170)
table.column("gender",width=170)
table.column("father name",width=170)
table.column("d.o.b",width=170)
table.column("contact",width=170)
table.column("address",width=170)

def add_student():
        # Empty field check
    if (e1.get()=="" or e2.get()=="" or combo.get()=="" or e4.get()=="" or e5.get()=="" or e6.get()=="" or address_txt.get("1.0", END)=="" ):

        messagebox.showerror(
            "Error",
            "Please fill all details"
        )
        return
    value=messagebox.askyesno("Information","Are all details correct?")
    if value:
         table.insert(
             "",
             END,
             values=(
                 e1.get(),
                 e2.get(),
                 combo.get(),
                 e4.get(),
                 e5.get(),
                 e6.get(),
                 address_txt.get("1.0", END)
            )
        )
         messagebox.showinfo("Information","Student Added Successfully")


#button
Button(root,text='ADD',font='impack 15 bold',bg='red',fg='white',width=30,height=1,bd=5,command=add_student).place(x=4,y=665)
def delete_student():

    selected = table.focus()

    if not selected:
        messagebox.showerror(
            "Error",
            "Please select a student"
        )
        return

    value = messagebox.askyesno(
        "Delete",
        "Are you sure you want to delete this student data?"
    )

    if value:
        table.delete(selected)
        messagebox.showinfo(
            "Success",
            "Student Data Deleted Successfully"
        )
Button(root,text='Delete Student',font='impack 15 bold',bg='yellow',fg='white',width=30,height=1,bd=5,command=delete_student).place(x=380,y=665)


def quit():
   value= messagebox.askyesno("Warning","Are you sure you want to close the window?")
   if value:
      root.destroy()
       
Button(root,text='Close window',font='impack 15 bold',bg='blue',fg='white',width=36,height=1,bd=5,command=quit).place(x=755,y=665)

root.mainloop()