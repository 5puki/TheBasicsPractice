from tkinter import *

def click1(event):
    login_entry.configure(state=NORMAL)
    login_entry.delete(0,END)
    login_entry.unbind("<Button-1>", clicked1)

def click2(event):
    pw_entry.configure(state=NORMAL)
    pw_entry.delete(0,END)
    pw_entry.unbind("<Button-1>", clicked2)

window = Tk()

window.title("Kick.com login window")
window_icon = PhotoImage(file="kick.png")
window.iconphoto(True, window_icon)
window.geometry("300x125")
#-----------------------------------------------------
login_label = Label(window,
                    text = "Kick.com",
                    font = ("Ariel", 30, "bold"),
                    bg = "black",
                    fg = "#39FF14")
login_label.pack()
#-----------------------------------------------------
login_entry = Entry(window,
                    width = 30,
                    bg = "black",
                    fg = "#39FF14")
login_entry.insert(0, "Enter Username Here")
login_entry.pack()

clicked1 = login_entry.bind("<Button-1>", click1)
#-----------------------------------------------------
pw_entry = Entry(window,
                 width = 30,
                 bg="black",
                 fg="#39FF14",
                 show = "*")
pw_entry.insert(0, "Enter Password Here")
pw_entry.pack()

clicked2 = pw_entry.bind("<Button-1>", click2)
#-----------------------------------------------------
login_button = Button(window,
                      text = "Login",
                      bg = "black",
                      fg = "#39FF14")
login_button.pack()
#-----------------------------------------------------


window.mainloop()