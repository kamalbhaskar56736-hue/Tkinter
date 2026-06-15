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
      messagebox.showinfo("Time Up", f"Your Score is {score}/{len(questions)}")
      win.destroy()
      return