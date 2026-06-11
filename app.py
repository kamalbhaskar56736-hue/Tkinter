from tkinter import *

root = Tk()
root.geometry("666x700")
root.title("My First GUI App")

label = Label(root, text="Zindagi mein kamyabi paane ke liye mehnat sabse zaroori hai.\n Mehnat ko kamyabi ki chabi (key) kaha jata hai.\n Duniya mein jitne bhi bade aur kamyab log hue hain, unhone apni zindagi mein bohot kadi mehnat ki hai. \nKoi bhi insan bina kaam kiye raat-o-raat bada nahi\n banta. Jab hum kisi kaam ko lagan aur imandari se karte hain, toh uska phal humein zaroor milta hai.\n Kuch log kismat ke bharose baithe rehte hain, lekin\n kismat bhi unhi ka sath deti hai jo khud koshish karte hain.\n Mehnat karne se na sirf humein hamara goal milta hai, balki hamara self-confidence bhi\n badhta hai. Mushkilein har kisi ki zindagi mein aati hain, lekin sachi mehnat se har\n mushkil ko door kiya ja sakta hai. Isliye, agar humein apna future \nbehtar banana hai, toh aalas ko chhodkar hamesha aage badhte rehna chahiye. \nMehnat kabhi bekar nahi jaati.", bg="red",fg="white",padx=99,pady=88,font="comicsansms 19 bold",borderwidth=20,relief="groove")
label.pack(fill="y")

root.mainloop()