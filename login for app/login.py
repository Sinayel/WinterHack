import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk

from PIL import Image, ImageTk

# Colors
co1 = "white"
co2 = "#C2C2C2"
co3 = "#6074FF"
co4 = "black"
co5 = "#FF665A"

# Font
Poppins12 = "Poppins 12"
Poppins23 = "Poppins 23"


class LoginApp(tk.Frame):
    # créer le contenu de la fenêtre
    def __init__(self, root):
        super().__init__(root)
        self.frame()

    def delete(self):
        self.window_success.destroy()

    # to be deleted (it's a page to see that you have been connected)
    def login_sucess(self):
        self.window_success = tk.Toplevel(window)
        self.window_success.title("Success")
        self.window_success.geometry('307x150')
        self.window_success.configure(bg=co1)

        # Frame up/down
        frame_up = Frame(self.window_success, width=310, height=50, bg=co1)
        frame_up.grid(row=0, column=0)
        frame_down = Frame(self.window_success, width=310, height=300, bg=co1)
        frame_down.grid(row=1, column=0)

        # Heading
        heading = Label(frame_up, text="Sucess", bg=co1, font=Poppins23)
        heading.place(x=99, y=5)

        line = Label(frame_up, width=40, text="", height=1, bg=co3, anchor=NW)
        line.place(x=10, y=45)

        # Button
        save = Button(frame_down, text="Close", width=9, height=1, font="arial 12 bold",
                      bg="lightblue", command=self.delete)
        save.place(x=99, y=40)

    def password_not_recognised(self):
        messagebox.showerror("Error", "the password was not recognized")

    def user_not_found(self):
        messagebox.showerror("Error", "the user has not been recognized")

    def login_verify(self):
        username1 = username_verify.get()
        password1 = password_verify.get()
        self.e_name.delete(0, END)
        self.e_password.delete(0, END)

        list_of_files = os.listdir('User')
        if username1 in list_of_files:
            file1 = open('User/' + username1, "r")
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
