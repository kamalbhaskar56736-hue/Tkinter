from tkinter import*
from tkinter import messagebox
root=Tk()
root.geometry("1030x780")
root.title("Quiz")
root.config(bg="lightblue")
Label(root,text=" Programming Quiz  ",font='impack 28 bold',fg="blue",bg="lightblue").place(x=300,y=2)


java = (
    (
        "1. Who is known as the Father of win?",
        ("Dennis Ritchie", "James Gosling", "Bjarne Stroustrup", "Guido van Rossum"),
        "James Gosling"
    ),
    (
        "2. What is the full form of JVM?",
        ("win Variable Machine", "win Virtual Machine", "win Verified Machine", "win Vendor Machine"),
        "win Virtual Machine"
    ),
    (
        "3. Which keyword is used for inheritance in win?",
        ("implements", "extends", "inherit", "super"),
        "extends"
    ),
    (
        "4. Which company originally developed win?",
        ("Microsoft", "Oracle", "Sun Microsystems", "IBM"),
        "Sun Microsystems"
    ),
    (
        "5. win is a _____ language.",
        ("Procedural", "Machine", "Object Oriented", "Assembly"),
        "Object Oriented"
    ),
    (
        "6. Which method starts a win program?",
        ("start()", "run()", "main()", "execute()"),
        "main()"
    ),
    (
        "7. Which keyword creates an object?",
        ("create", "new", "class", "object"),
        "new"
    ),
    (
        "8. Which package is imported automatically?",
        ("java.io", "java.util", "java.lang", "java.net"),
        "java.lang"
    ),
    (
        "9. win source file extension is?",
        (".class", ".exe", ".java", ".jar"),
        ".java"
    ),
    (
        "10. win bytecode extension is?",
        (".java", ".jar", ".class", ".txt"),
        ".class"
    ),
    (
        "11. Which operator compares values?",
        ("=", "==", "!=", ":="),
        "=="
    ),
    (
        "12. Which loop executes at least once?",
        ("for", "while", "do-while", "foreach"),
        "do-while"
    ),
    (
        "13. Which keyword refers to current object?",
        ("self", "this", "super", "current"),
        "this"
    ),
    (
        "14. Which keyword refers to parent class?",
        ("this", "parent", "extends", "super"),
        "super"
    ),
    (
        "15. Which access modifier is most restrictive?",
        ("public", "protected", "private", "default"),
        "private"
    ),
    (
        "16. Which access modifier is accessible everywhere?",
        ("private", "default", "protected", "public"),
        "public"
    ),
    (
        "17. Which keyword makes a variable constant?",
        ("fixed", "const", "final", "static"),
        "final"
    ),
    (
        "18. win supports?",
        ("Single Thread", "Multithreading", "No Thread", "None"),
        "Multithreading"
    ),
    (
        "19. Which statement exits a loop?",
        ("continue", "stop", "break", "exit"),
        "break"
    ),
    (
        "20. Which statement skips an iteration?",
        ("break", "continue", "stop", "exit"),
        "continue"
    ),
    (
        "21. Array index starts from?",
        ("1", "0", "-1", "2"),
        "0"
    ),
    (
        "22. Which class is parent of all classes?",
        ("Main", "Object", "Parent", "Root"),
        "Object"
    ),
    (
        "23. Which package contains Scanner?",
        ("java.io", "java.util", "java.net", "java.lang"),
        "java.util"
    ),
    (
        "24. Scanner is used for?",
        ("Output", "Input", "Database", "Network"),
        "Input"
    ),
    (
        "25. Which method prints output?",
        ("echo()", "print()", "System.out.println()", "cout"),
        "System.out.println()"
    ),
    (
        "26. Constructor name must match?",
        ("Method", "Class", "Package", "Object"),
        "Class"
    ),
    (
        "27. Which keyword is used for abstraction?",
        ("abstract", "virtual", "hidden", "define"),
        "abstract"
    ),
    (
        "28. Multiple inheritance is achieved using?",
        ("Class", "Object", "Interface", "Constructor"),
        "Interface"
    ),
    (
        "29. Which keyword defines an interface?",
        ("class", "interface", "abstract", "define"),
        "interface"
    ),
    (
        "30. Which exception occurs on divide by zero?",
        ("IOException", "ArithmeticException", "ArrayException", "NullPointerException"),
        "ArithmeticException"
    ),
    (
        "31. Which block always executes?",
        ("try", "catch", "finally", "throw"),
        "finally"
    ),
    (
        "32. Which keyword throws an exception?",
        ("catch", "throw", "throws", "error"),
        "throw"
    ),
    (
        "33. Which collection stores unique values?",
        ("List", "Array", "Set", "Vector"),
        "Set"
    ),
    (
        "34. Which collection allows duplicates?",
        ("Set", "Map", "List", "TreeSet"),
        "List"
    ),
    (
        "35. String length method is?",
        ("size()", "count()", "len()", "length()"),
        "length()"
    ),
    (
        "36. Which company owns win today?",
        ("IBM", "Google", "Oracle", "Microsoft"),
        "Oracle"
    ),
    (
        "37. win follows?",
        ("WORA", "WOA", "WRA", "WORAA"),
        "WORA"
    ),
    (
        "38. Which keyword is used to import packages?",
        ("package", "include", "import", "using"),
        "import"
    ),
    (
        "39. Which keyword creates packages?",
        ("module", "package", "include", "import"),
        "package"
    ),
    (
        "40. Which method starts a thread?",
        ("run()", "begin()", "execute()", "start()"),
        "start()"
    ),
    (
        "41. Which loop is best when count is known?",
        ("while", "do-while", "for", "switch"),
        "for"
    ),
    (
        "42. Which statement is used for selection?",
        ("if", "for", "while", "break"),
        "if"
    ),
    (
        "43. win is platform?",
        ("Dependent", "Independent", "Specific", "Limited"),
        "Independent"
    ),
    (
        "44. Which keyword is used with classes?",
        ("class", "struct", "define", "module"),
        "class"
    ),
    (
        "45. Which symbol ends a statement?",
        (".", ":", ";", ","),
        ";"
    ),
    (
        "46. Which type stores true/false?",
        ("int", "char", "boolean", "float"),
        "boolean"
    ),
    (
        "47. Which operator means NOT equal?",
        ("==", "!=", "=", "<>"),
        "!="
    ),
    (
        "48. Which keyword is used for inheritance implementation?",
        ("extends", "implements", "super", "this"),
        "implements"
    ),
    (
        "49. Which keyword is used to stop a method and return value?",
        ("break", "continue", "return", "exit"),
        "return"
    ),
    (
        "50. win is compiled into?",
        ("Machine Code", "Source Code", "Bytecode", "Assembly"),
        "Bytecode"
    )
)
python = (
    (
        "1. Who developed Python?",
        ("Dennis Ritchie", "James Gosling", "Guido van Rossum", "Bjarne Stroustrup"),
        "Guido van Rossum"
    ),
    (
        "2. Python was released in?",
        ("1989", "1991", "1995", "2000"),
        "1991"
    ),
    (
        "3. Which symbol is used for comments?",
        ("//", "#", "/*", "--"),
        "#"
    ),
    (
        "4. Which function prints output?",
        ("echo()", "display()", "print()", "show()"),
        "print()"
    ),
    (
        "5. Which function takes input?",
        ("scan()", "input()", "get()", "read()"),
        "input()"
    ),
    (
        "6. Python is a _____ language.",
        ("Compiled", "Assembly", "Interpreted", "Machine"),
        "Interpreted"
    ),
    (
        "7. List is represented by?",
        ("{}", "()", "[]", "<>"),
        "[]"
    ),
    (
        "8. Tuple is represented by?",
        ("[]", "{}", "()", "<>"),
        "()"
    ),
    (
        "9. Dictionary is represented by?",
        ("[]", "{}", "()", "<>"),
        "{}"
    ),
    (
        "10. Which keyword defines a function?",
        ("function", "fun", "def", "define"),
        "def"
    ),
    (
        "11. Which keyword defines a class?",
        ("class", "define", "object", "struct"),
        "class"
    ),
    (
        "12. Which keyword creates inheritance?",
        ("extends", "inherit", ":", "super"),
        ":"
    ),
    (
        "13. Which data type stores True/False?",
        ("int", "bool", "str", "float"),
        "bool"
    ),
    (
        "14. len() is used for?",
        ("Addition", "Length", "Input", "Output"),
        "Length"
    ),
    (
        "15. Which loop is used for iteration?",
        ("for", "switch", "goto", "case"),
        "for"
    ),
    (
        "16. Which loop works on condition?",
        ("while", "case", "goto", "switch"),
        "while"
    ),
    (
        "17. Which keyword exits a loop?",
        ("continue", "stop", "break", "exit"),
        "break"
    ),
    (
        "18. Which keyword skips an iteration?",
        ("continue", "break", "stop", "return"),
        "continue"
    ),
    (
        "19. Python file extension?",
        (".java", ".py", ".js", ".cpp"),
        ".py"
    ),
    (
        "20. Which function converts string to integer?",
        ("str()", "float()", "int()", "bool()"),
        "int()"
    ),
    (
        "21. Which function converts integer to string?",
        ("str()", "float()", "int()", "bool()"),
        "str()"
    ),
    (
        "22. Which keyword handles exceptions?",
        ("catch", "except", "error", "handle"),
        "except"
    ),
    (
        "23. Which block always runs?",
        ("except", "finally", "try", "raise"),
        "finally"
    ),
    (
        "24. Python supports OOP?",
        ("No", "Yes", "Partially", "Limited"),
        "Yes"
    ),
    (
        "25. Which keyword creates an object?",
        ("new", "create", "ClassName()", "object"),
        "ClassName()"
    )
)
javascript = (
    (
        "1. Who developed JavaScript?",
        ("Brendan Eich", "James Gosling", "Guido van Rossum", "Dennis Ritchie"),
        "Brendan Eich"
    ),
    (
        "2. JavaScript was created in?",
        ("1995", "1991", "2000", "1985"),
        "1995"
    ),
    (
        "3. JavaScript file extension is?",
        (".java", ".py", ".js", ".jsx"),
        ".js"
    ),
    (
        "4. Which tag is used for JavaScript in HTML?",
        ("<java>", "<script>", "<js>", "<javascript>"),
        "<script>"
    ),
    (
        "5. Which function prints output in browser?",
        ("print()", "console.log()", "echo()", "show()"),
        "console.log()"
    ),
    (
        "6. Which keyword declares a variable?",
        ("var", "int", "string", "float"),
        "var"
    ),
    (
        "7. Modern variable keyword is?",
        ("let", "int", "float", "char"),
        "let"
    ),
    (
        "8. Constant variable keyword?",
        ("let", "var", "const", "fixed"),
        "const"
    ),
    (
        "9. Which symbol is used for comments?",
        ("#", "//", "--", "**"),
        "//"
    ),
    (
        "10. JavaScript is a _____ language.",
        ("Compiled", "Interpreted", "Assembly", "Machine"),
        "Interpreted"
    ),
    (
        "11. Which function shows alert box?",
        ("alert()", "message()", "show()", "popup()"),
        "alert()"
    ),
    (
        "12. Which keyword defines a function?",
        ("func", "define", "function", "method"),
        "function"
    ),
    (
        "13. Which operator compares value and type?",
        ("==", "=", "===", "!="),
        "==="
    ),
    (
        "14. Which loop repeats code?",
        ("for", "switch", "case", "goto"),
        "for"
    ),
    (
        "15. Which statement is used for condition?",
        ("if", "loop", "switch", "goto"),
        "if"
    ),
    (
        "16. Which statement handles multiple choices?",
        ("if", "switch", "loop", "case"),
        "switch"
    ),
    (
        "17. Which keyword exits a loop?",
        ("continue", "break", "stop", "exit"),
        "break"
    ),
    (
        "18. Which keyword skips an iteration?",
        ("continue", "break", "stop", "return"),
        "continue"
    ),
    (
        "19. Which method converts string to integer?",
        ("int()", "parseInt()", "str()", "number()"),
        "parseInt()"
    ),
    (
        "20. Which method converts to float?",
        ("float()", "parseFloat()", "number()", "decimal()"),
        "parseFloat()"
    ),
    (
        "21. JavaScript runs inside?",
        ("Compiler", "Browser", "Database", "Server Only"),
        "Browser"
    ),
    (
        "22. DOM stands for?",
        ("Document Object Model", "Data Object Model", "Display Object Model", "Document Output Model"),
        "Document Object Model"
    ),
    (
        "23. Which method selects element by id?",
        ("getElement()", "getElementById()", "query()", "select()"),
        "getElementById()"
    ),
    (
        "24. Which event occurs on button click?",
        ("onhover", "onclick", "onload", "onchange"),
        "onclick"
    ),
    (
        "25. JavaScript supports OOP?",
        ("No", "Yes", "Limited", "Partial"),
        "Yes"
    )
)


def start_quiz(questions, title):
    win = Toplevel(root)
    win.config(bg="lightblue")
    win.geometry("1050x790")
    win.title(title)
#Timer set===================================================================================================================================
    def countdown():
     nonlocal time_left

     if time_left > 0:
        timer_label.config(text=f"Time Left: {time_left}")
        time_left -= 1
        win.after(   1000,countdown)

     else:
      win.destroy()
      show_result(score, len(questions))
      
#===========================================================================================================================================
    current_question = 0
    score = 0
    time_left = 60
#frame-----------------------------------------------------------------------------------------
    top_frame = Frame(win, bg="lightblue")
    top_frame.pack(fill="x")
#--------------------------------------------------------------------------------------------------
    timer_label = Label(top_frame,text="Time Left: 60",font=("Arial",16,"bold"),fg="black",bg="lightblue")
    timer_label.pack(side="right",anchor="n")
#total questions====================================================================================================================
    total=Label(top_frame,text=f"Total Questions:{len(questions)}",fg="black",font=("Arial",16,"bold"),bg="lightblue")
    total.pack(side="right",anchor="n")
#========================================================================================================================================
    answer = StringVar()
    question_label = Label(win,text="",font=("Arial", 20, "bold"),bg="lightblue",wraplength=900)
    question_label.pack(pady=40)

    r1 = Radiobutton(win, variable=answer, font=("Arial", 16),bg="lightblue")
    r2 = Radiobutton(win, variable=answer, font=("Arial", 16),bg="lightblue")
    r3 = Radiobutton(win, variable=answer, font=("Arial", 16),bg="lightblue")
    r4 = Radiobutton(win, variable=answer, font=("Arial", 16),bg="lightblue")

    r1.pack(anchor="w", padx=50, pady=5)
    r2.pack(anchor="w", padx=50, pady=5)
    r3.pack(anchor="w", padx=50, pady=5)
    r4.pack(anchor="w", padx=50, pady=5)

    def load_question():

        question_label.config(text=questions[current_question][0])

        r1.config(text=questions[current_question][1][0],value=questions[current_question][1][0] )
        r2.config(text=questions[current_question][1][1],value=questions[current_question][1][1])
        r3.config(text=questions[current_question][1][2],value=questions[current_question][1][2])
        r4.config(text=questions[current_question][1][3],value=questions[current_question][1][3])

        answer.set("")


#next button===============================================================================================================================        

    def next_question():

        nonlocal current_question
        nonlocal score

        if answer.get() == "":
            messagebox.showerror("Error","Please select an answer")
            return

        if answer.get() == questions[current_question][2]:
            score += 1

        current_question += 1

        if current_question < len(questions):
            load_question()

        else:
            win.destroy()
            show_result(score, len(questions))

    def exit_quiz():
     value = messagebox.askyesno("Exit","Are you sure you want to exit the quiz?")
     if value:
        win.destroy()

    Button(top_frame,text="Exit Quiz",bg="red",command=exit_quiz).pack(side=RIGHT, padx=15,anchor="n")

#bottom Frame
    bottom_frame = Frame(win,bg="lightblue")
    bottom_frame.pack(pady=20)
    Button(bottom_frame,text="Save",font=("Arial",16,"bold"),bg="yellow").pack(side=LEFT,padx=10)
    Button(bottom_frame,text="Next",font=("Arial",16,"bold"),bg="red",command=next_question).pack(side=LEFT,padx=10)
   
    load_question()
    countdown()

#==================================================================================================================================================
def open_quiz():

    quiz = Toplevel(root)
    quiz.geometry("1050x790")
    quiz.config(bg="lightblue")
    quiz.title("Quiz Test")

    Button(quiz,text='JAVA',font='impack 18 bold',bg='blue',fg='white',width=36,height=2,bd=5,command=lambda: start_quiz(java, "win Quiz")).place(x=300,y=200)
    Button(quiz,text='PYTHON',font='impack 18 bold',bg='green',fg='white',width=36,height=2,bd=5,command=lambda: start_quiz(python, "Python Quiz")).place(x=300,y=300)
    Button(quiz,text='JAVASCRIPT',font='impack 18 bold',bg='red',fg='white',width=36,height=2,bd=5,command=lambda: start_quiz(javascript, "JavaScript Quiz")).place(x=300,y=400)

#------------------------------------------------------------------------------------------------------------------------------------------------    

#Registration ------------------------------------------------------------------------==========================================================
f1=LabelFrame(root,text='Registration',borderwidth=4,font='impack 28 bold',bg="grey",bd=5)
f1.place(x=250,y=50, width=500, height=700)
Label(f1,text="Name:",font='impack 20 bold',bg="grey").place(x=0,y=45)
Label(f1,text="D.O.B:",font='impack 20 bold',bg="grey").place(x=0,y=145)
Label(f1,text="Email:",font='impack 20 bold',bg="grey").place(x=0,y=245)
Label(f1,text="Mobile No.:",font='impack 20 bold',bg="grey").place(x=0,y=345)
Label(f1,text="Password:",font='impack 20 bold',bg="grey").place(x=0,y=445)

#entry
e1=Entry(f1,bd=1,font='impack 20 bold',width=20)
e1.place(x=130,y=45)
e2=Entry(f1,bd=1,font='impack 20 bold',width=20)
e2.place(x=130,y=145)
e3=Entry(f1,bd=1,font='impack 20 bold',width=20)
e3.place(x=130,y=245)
e4=Entry(f1,bd=1,font='impack 20 bold',width=18)
e4.place(x=160,y=345)
e5=Entry(f1,bd=1,font='impack 20 bold',width=18,show="*")

e5.place(x=160,y=445)


#-------------------------------------------------------------------------------------

def submit():
    if e1.get()=="" or e2.get()=="" or e3.get()=="" or e4.get()=="" or e5.get()=="":
     messagebox.showerror("Error","Please fill all details")
    else:
       value=messagebox.askyesno("Information","Are all details correct?")
       if value:
          messagebox.showinfo("Information","Student Added Successfully")
          ready=value=messagebox.askyesno("Info","Are you ready for exam?")
          if ready:
             open_quiz()
             root.withdraw()
             
Button(f1,text="Sumbit",font='impack 20 bold',bg="lightblue",command=submit).place(x=150,y=580,width=200)

#result---------------------------------------------------------------------------------

def show_result(score, total):
    result = Toplevel(root)
    result.geometry("500x400")
    result.title("Quiz Result")
    result.config(bg="lightgreen")

    percentage = (score / total) * 100

    Label(result,text="QUIZ RESULT",font=("Arial", 24, "bold"),bg="lightgreen",fg="blue").pack(pady=20)

    Label(result,text=f"Score: {score}/{total}",font=("Arial", 18, "bold"),bg="lightgreen").pack(pady=10)

    Label(result,text=f"Percentage: {percentage:.2f}%",font=("Arial", 18, "bold"),bg="lightgreen").pack(pady=10)

    if percentage >= 40:
        result_text = "PASS "
        color = "green"
    else:
        result_text = "FAIL "
        color = "red"

    Label(result,text=result_text,font=("Arial", 22, "bold"),fg=color,bg="lightgreen"
    ).pack(pady=20)

    Button(result,text="Close",command=result.destroy,bg="red",fg="white").pack(pady=20)
root.mainloop()