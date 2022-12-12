import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
import webbrowser

from PIL import Image, ImageTk

# Colors
co1 = "white"
co2 = "#C2C2C2"
co3 = "#6074FF"
co4 = "black"
co5 = "#FF665A"

HEIGHT = 700
WIDTH = 1200

# Font
Poppins12 = "Poppins 12"
Poppins23 = "Poppins 23"


class LoginApp(tk.Frame):
    # créer le contenu de la fenêtre
    def __init__(self, root):
        super().__init__(root)
        self.frame()

    # to be deleted (it's a page to see that you have been connected)

    def open_home(self):
        self.homePage.lift()
        self.home["relief"] = "sunken"
        self.myChatrooms["relief"] = "raised"
        self.exercises["relief"] = "raised"
        self.help_r["relief"] = "raised"
        self.settings["relief"] = "raised"

    def open_chat(self):
        self.chatPage.lift()
        self.home["relief"] = "raised"
        self.myChatrooms["relief"] = "sunken"
        self.exercises["relief"] = "raised"
        self.help_r["relief"] = "raised"
        self.settings["relief"] = "raised"

    def open_exercises(self):
        self.exercisePage.lift()
        self.home["relief"] = "raised"
        self.myChatrooms["relief"] = "raised"
        self.exercises["relief"] = "sunken"
        self.help_r["relief"] = "raised"
        self.settings["relief"] = "raised"

    def open_settings(self):
        self.settingsPage.lift()
        self.home["relief"] = "raised"
        self.myChatrooms["relief"] = "raised"
        self.exercises["relief"] = "raised"
        self.help_r["relief"] = "raised"
        self.settings["relief"] = "sunken"

    def open_help(self):
        self.helpPage.lift()
        self.home["relief"] = "raised"
        self.myChatrooms["relief"] = "raised"
        self.exercises["relief"] = "raised"
        self.help_r["relief"] = "sunken"
        self.settings["relief"] = "raised"

    def open_reportForm(self):
        webbrowser.open("https://forms.gle/mqzgpgpWHABrVEjo7")

    def login_sucess(self):
        self.root = tk.Toplevel(window)

        username = self.username1
        exp = 10
        lvl = 20

        # Accuracy is calculated by taking the percentage of questions the user answered correctly within the past 50 exercises
        acc = 78
        pfp = tk.PhotoImage(file="defaultpfp.png")

        # canvas is primarily for drawing shapes and things
        canvas = tk.Canvas(self.root, height=HEIGHT, width=WIDTH)
        canvas.pack()

        # main frames/blocks
        self.sidebar = tk.Frame(self.root, bg="#c3d1fb")
        self.sidebar.place(relx=0, rely=0, relwidth=0.2, relheight=1)

        self.topbar = tk.Frame(self.root, bg="#6074FF")
        self.topbar.place(relx=0, rely=0, relwidth=1, relheight=0.12)

        self.mainFrame = tk.Frame(self.root, bg="#e8ebee")
        self.mainFrame.place(relx=0.2, rely=0.12, relwidth=0.8, relheight=0.88)

        # Pages
        self.settingsPage = tk.Frame(self.mainFrame, bg="yellow")
        self.settingsPage.place(relx=0, rely=0, relheight=1, relwidth=1)

        self.helpPage = tk.Frame(self.mainFrame, bg="#e8ebee")
        self.helpPage.place(relx=0, rely=0, relheight=1, relwidth=1)

        self.chatPage = tk.Frame(self.mainFrame, bg="gray")
        self.chatPage.place(relx=0, rely=0, relheight=1, relwidth=1)

        self.exercisePage = tk.Frame(self.mainFrame, bg="blue")
        self.exercisePage.place(relx=0, rely=0, relheight=1, relwidth=1)

        self.homePage = tk.Frame(self.mainFrame, bg="#e8ebee")
        self.homePage.place(relx=0, rely=0, relheight=1, relwidth=1)

        # Topbar Contents
        self.reportBug = tk.Button(self.topbar, text="Report an Issue", anchor="w", font=("Cambria", 13), fg="white",
                                   bg="#6074FF",
                                   borderwidth=0, command=self.open_reportForm)
        self.reportBug.place(relx=0.88, rely=0.2, relwidth=0.1, relheight=0.6)

        self.logo = tk.PhotoImage(file="logo.png")
        logoButton = tk.Button(self.topbar, image=self.logo, relief="groove", bg="#6074FF", bd="0")
        logoButton.place(relx=0, rely=0, relwidth=0.2, relheight=1)

        # Sidebar Contents

        self.pfp = tk.Label(self.sidebar, image=pfp, bg="white")
        self.pfp.place(relx=0.2, rely=0.15, relwidth=0.6, relheight=0.2)

        self.home = tk.Button(self.sidebar, text="Home", background="#ebefff", font=("Cambria", 12),
                              activebackground="#e8ebee",
                              relief="sunken", command=self.open_home)
        self.home.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.05)

        self.myChatrooms = tk.Button(self.sidebar, text="My Chatrooms", background="#ebefff", font=("Cambria", 12),
                                     activebackground="#e8ebee", command=self.open_chat)
        self.myChatrooms.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.05)

        self.exercises = tk.Button(self.sidebar, text="Exercises", background="#ebefff", font=("Cambria", 12),
                                   activebackground="#e8ebee",
                                   command=self.open_exercises)
        self.exercises.place(relx=0.1, rely=0.6, relwidth=0.8, relheight=0.05)

        self.help_r = tk.Button(self.sidebar, text="Help", background="#ebefff", font=("Cambria", 12),
                                activebackground="#e8ebee",
                                command=self.open_help)
        self.help_r.place(relx=0.1, rely=0.7, relwidth=0.8, relheight=0.05)

        self.settings = tk.Button(self.sidebar, text="Settings", background="#ebefff", font=("Cambria", 12),
                                  activebackground="#e8ebee",
                                  command=self.open_settings)
        self.settings.place(relx=0.1, rely=0.8, relwidth=0.8, relheight=0.05)

        # -------------------------------------------------------------------------
        # HOMEPAGE Mainframe contents

        self.welcomeFrame = tk.Frame(self.homePage, bg="white", relief="ridge", borderwidth=2)
        self.welcomeFrame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.2)

        welcome = tk.Label(self.welcomeFrame, text="Welcome, " + username + "!", font=("Cambria bold", 36),
                           anchor="w",
                           padx=20,
                           bg="white")
        welcome.place(relx=0.02, rely=0.05, relwidth=0.96, relheight=0.9)

        self.recFrame = tk.Frame(self.homePage, bg="white", relief="ridge", borderwidth=2)
        self.recFrame.place(relx=0.05, rely=0.3, relwidth=0.9, relheight=0.6)

        self.expGraphic = tk.PhotoImage(file="exp.png")
        self.expPic = tk.Label(self.recFrame, bg="white", image=self.expGraphic)
        self.expPic.place(relx=0.1, rely=0.2, relwidth=0.2, relheight=0.5)
        self.expText = tk.Label(self.recFrame, bg="white", text="Total XP: " + str(exp), font=("Cambria", 16))
        self.expText.place(relx=0.1, rely=0.05, relwidth=0.2, relheight=0.2)
        self.expInfo = tk.Label(self.recFrame, bg="white", text="Harder questions grant more xp!", font=("Cambria", 8))
        self.expInfo.place(relx=0.1, rely=0.68, relwidth=0.2, relheight=0.1)

        self.lvlGraphic = tk.PhotoImage(file="lvl.png")
        self.lvlPic = tk.Label(self.recFrame, bg="white", image=self.lvlGraphic)
        self.lvlPic.place(relx=0.4, rely=0.2, relwidth=0.2, relheight=0.5)
        self.lvlText = tk.Label(self.recFrame, bg="white", text="Current LVL: " + str(lvl), font=("Cambria", 16))
        self.lvlText.place(relx=0.4, rely=0.05, relwidth=0.2, relheight=0.2)
        self.lvlInfo = tk.Label(self.recFrame, bg="white", text="Complete exercises to level up!", font=("Cambria", 8))
        self.lvlInfo.place(relx=0.4, rely=0.68, relwidth=0.2, relheight=0.1)

        accGraphic = tk.PhotoImage(file="acc.png")
        self.accPic = tk.Label(self.recFrame, bg="white", image=accGraphic)
        self.accPic.place(relx=0.7, rely=0.2, relwidth=0.2, relheight=0.5)
        self.accText = tk.Label(self.recFrame, bg="white", text="Exercise ACC: " + str(acc) + "%",
                                font=("Cambria", 16))
        self.accText.place(relx=0.7, rely=0.05, relwidth=0.2, relheight=0.2)
        self.accInfo = tk.Label(self.recFrame, bg="white", text="Based on the last 50 exercises!", font=("Cambria", 8))
        self.accInfo.place(relx=0.7, rely=0.68, relwidth=0.2, relheight=0.1)

        self.exercisesButton = tk.Button(self.recFrame, bg="white", text="Begin Exercises", font=("Cambria", 12),
                                         command=self.open_exercises)
        self.exercisesButton.place(relx=0.1, rely=0.84, relwidth=0.38, relheight=0.1)

        self.chatButton = tk.Button(self.recFrame, bg="white", text="Practice with a native speaker",
                                    font=("Cambria", 12),
                                    command=self.open_chat)
        self.chatButton.place(relx=0.52, rely=0.84, relwidth=0.38, relheight=0.1)

        # HELPPAGE Mainframe contents

        self.titleFrame = tk.Frame(self.helpPage, bg="white", relief="ridge", borderwidth=2)
        self.titleFrame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.28)
        self.titleText = tk.Label(self.titleFrame, bg="white", text="New to WorldSpeak?", font=("Cambria bold", 36),
                                  anchor="w",
                                  padx=20)
        self.titleText.place(relx=0.02, rely=0, relwidth=0.96, relheight=0.85)
        self.subtitleText = tk.Label(self.titleFrame, bg="white", text="We're here to help!", font=("Cambria bold", 16),
                                     anchor="w",
                                     padx=20)
        self.subtitleText.place(relx=0.02, rely=0.64, relwidth=0.96, relheight=0.15)

        self.scrollFrame = tk.Frame(self.helpPage, bg="white", relief="ridge", borderwidth=2)
        self.scrollFrame.place(relx=0.05, rely=0.38, relwidth=0.9, relheight=0.52)

        # tutorial=tk.Label(scrollFrame, font=("Cambria",12))

        self.T = tk.Text(self.scrollFrame)
        self.scroll = tk.Scrollbar(self.T)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.T.place(relheight=0.9, relwidth=0.9, relx=0.05, rely=0.05)
        self.scroll.config(command=self.T.yview)
        self.T.config(yscrollcommand=self.scroll.set)
        self.quote = """Welcome to WorldSpeak! This is an application designed to assist 
        Whether 'tis nobler in the mind to suffer
        The slings and arrows of outrageous fortune
        Or to take arms against a sea of troubles
        And by opposing end them. To die, to sleep--
        No more--and by a sleep to say we end
        The heartache, and the thousand natural shocks
        That flesh is heir to. 'Tis a consummation
        Devoutly to be wished."""
        self.T.insert(tk.END, self.quote)
        self.T.config(state="disabled")

        self.root.title("WorldSpeak")

        self.root.mainloop()

    def password_not_recognised(self):
        messagebox.showerror("Error", "the password was not recognized")

    def user_not_found(self):
        messagebox.showerror("Error", "the user has not been recognized")

    def login_verify(self):
        self.username1 = username_verify.get()
        password1 = password_verify.get()
        self.e_name.delete(0, END)
        self.e_password.delete(0, END)

        list_of_files = os.listdir('User')
        if self.username1 in list_of_files:
            file1 = open('User/' + self.username1, "r")
            verify = file1.read().splitlines()
            if password1 in verify:
                self.login_sucess()
            else:
                self.password_not_recognised()
        else:
            self.user_not_found()

    def register_info(self):
        global username_info
        global password_info
        global conditions_info
        username_info = username.get()
        password_info = password.get()
        condition_info = conditions.get()

        file = open("User/" + username_info, "w")
        file.write(username_info + "\n")
        file.write(password_info + "\n")
        file.write(str(True))
        file.close()

        self.r_name.delete(0, END)
        self.r_password.delete(0, END)

        msg = Label(self.window_register, text="Register success", fg='green')
        msg.place(x=120, y=60)

    def register_app(self):
        self.window_register = tk.Toplevel(window)
        self.window_register.title("Register")
        self.window_register.geometry('407x350')
        self.window_register.resizable(width=False, height=False)
        self.window_register.configure(bg=co1)

        # Frame up/down
        frame_up = Frame(self.window_register, width=310, height=50, bg=co1)
        frame_up.grid(row=0, column=0)
        frame_down = Frame(self.window_register, width=310, height=300, bg=co1)
        frame_down.grid(row=1, column=0)

        # Heading
        heading = Label(frame_up, text="SIGN UP", bg=co1, font=Poppins23)
        heading.place(x=99, y=5)

        line = Label(frame_up, width=40, text="", height=1, bg=co3, anchor=NW)
        line.place(x=10, y=45)

        # Name/Password
        global username
        global password
        global conditions
        username = StringVar()
        password = StringVar()
        conditions = BooleanVar()

        # Name/Password entry
        self.r_name = Entry(frame_down, width=25, justify='left', font=("Microsoft YaHei UI Light", 15),
                            bg=co2, fg=co4, highlightthickness=1, textvariable=username)
        self.r_name.insert(0, "Username")
        self.r_name.bind('<FocusIn>', self.on_enter_name_r)
        self.r_name.bind('<FocusOut>', self.on_leave_name_r)
        self.r_name.place(x=14, y=42)

        self.r_password = Entry(frame_down, width=25, justify='left', font=("Microsoft YaHei UI Light", 15),
                                bg=co2, fg=co4, highlightthickness=1, textvariable=password)
        self.r_password.bind('<FocusIn>', self.on_enter_password_r)
        self.r_password.bind('<FocusOut>', self.on_leave_password_r)
        self.r_password.insert(0, "Password")
        self.r_password.place(x=14, y=90)

        # Button conditions/login
        checkButton = ttk.Checkbutton(frame_down, text="terms and conditions")
        checkButton.place(x=15, y=140)

        button_login = Button(frame_down, text="Login", bg=co3, fg=co1, width=39, height=2, font="Ivy 9 bold",
                              command=self.register_info, relief="flat")
        button_login.place(x=15, y=180)

        # Image
        self.img = PhotoImage(file="Images/userr.png")
        self.lbl = Label(self.window_register, bg=co1, image=self.img, width=100, height=100)
        self.lbl.place(x=299, y=1)

        # Button image
        upload = Button(self.window_register, text="Upload", width=9, height=1, font="arial 12 bold",
                        bg="lightblue", command=self.image_upload)
        upload.place(x=300, y=110)

        save = Button(self.window_register, text="Save", width=9, height=1, font="arial 12 bold",
                      bg="lightblue", command=self.Save)
        save.place(x=300, y=150)

        reset = Button(self.window_register, text="Reset", width=9, height=1,
                       font="arial 12 bold", bg=co5, command=self.Clear)
        reset.place(x=300, y=190)

    # For register
    def on_enter_name_r(self, n):
        self.r_name.delete(0, 'end')

    def on_leave_name_r(self, n):
        name = self.r_name.get()
        if name == '':
            self.r_name.insert(0, 'Username')

    def on_enter_password_r(self, p):
        self.r_password.delete(0, 'end')

    def on_leave_password_r(self, p):
        name = self.r_password.get()
        if name == '':
            self.r_password.insert(0, 'Password')

    # For login
    def on_enter_name(self, n):
        self.e_name.delete(0, 'end')

    def on_leave_name(self, n):
        name = self.e_name.get()
        if name == '':
            self.e_name.insert(0, 'Username')

    def on_enter_password(self, p):
        self.e_password.delete(0, 'end')

    def on_leave_password(self, p):
        name = self.e_password.get()
        if name == '':
            self.e_password.insert(0, 'Password')

    def Save(self):
        self.img2.save('User_image/' + str(self.photo2) + ".png")

    def Clear(self):
        img1 = PhotoImage(file='Images/userr.png')
        self.lbl.config(image=img1)
        self.lbl.image = img1
        img1 = ""

    def image_upload(self):
        self.file_upload = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select image file",
                                                      filetypes=(("PNG File", "*.png"),
                                                                 ("JPG File", "*.jpg"),
                                                                 ("All files", "*.txt")))
        self.img2 = Image.open(self.file_upload)
        self.resized_image = self.img2.resize((100, 100))
        self.photo2 = ImageTk.PhotoImage(self.resized_image)
        self.lbl.config(image=self.photo2)
        self.lbl.image = self.photo2

    def frame(self):
        # Name/Password
        global username_verify
        global password_verify

        username_verify = StringVar()
        password_verify = StringVar()

        # Frame up and down login
        self.frame_up = Frame(window, width=310, height=50, bg=co1)
        self.frame_up.grid(row=0, column=0)

        self.frame_down = Frame(window, width=310, height=300, bg=co1)
        self.frame_down.grid(row=1, column=0)

        # Frame up
        heading = Label(self.frame_up, text="LOGIN", bg=co1, font=Poppins23)
        heading.place(x=99, y=5)

        line = Label(self.frame_up, width=40, text="", height=1, bg=co3, anchor=NW)
        line.place(x=10, y=45)

        # Enter name/Password
        self.e_name = Entry(self.frame_down, width=25, justify='left', font=("Microsoft YaHei UI Light", 15),
                            bg=co2, fg=co4, highlightthickness=1, textvariable=username_verify)
        self.e_name.insert(0, "Username")
        self.e_name.bind('<FocusIn>', self.on_enter_name)
        self.e_name.bind('<FocusOut>', self.on_leave_name)
        self.e_name.place(x=14, y=42)

        self.e_password = Entry(self.frame_down, width=25, justify='left', font=("Microsoft YaHei UI Light", 15),
                                bg=co2, fg=co4, highlightthickness=1, textvariable=password_verify)
        self.e_password.bind('<FocusIn>', self.on_enter_password)
        self.e_password.bind('<FocusOut>', self.on_leave_password)
        self.e_password.insert(0, "Password")
        self.e_password.place(x=14, y=90)

        # Button login
        button_login = Button(self.frame_down, text="next", bg=co3, fg=co1, width=39, height=2, font="Ivy 9 bold",
                              command=self.login_verify, relief="flat")
        button_login.place(x=15, y=180)

        # Button register
        button_register = Button(self.frame_down, text="Sign up", bg=co1, fg=co3, width=10, height=1,
                                 font="Ivy 9 bold", command=self.register_app, relief="flat")
        button_register.place(x=133, y=228)

        label = tk.Label(self.frame_down, text="Don't have an account ?", bg=co1)
        label.place(x=15, y=230)


window = tk.Tk()
window.title("Login")
window.geometry('307x350')
window.resizable(width=False, height=False)
window.configure(bg=co1)
LoginApp(window)
window.mainloop()
