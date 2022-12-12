import tkinter as tk
import webbrowser
from googletrans import Translator
from csv import DictReader
from random import randint, choice

HEIGHT = 700
WIDTH = 1200
xpval=0
exp=0

def open_home():
    homePage.lift()
    home["relief"] = "sunken"
    myChatrooms["relief"] = "raised"
    exercises["relief"] = "raised"
    help["relief"] = "raised"
    settings["relief"] = "raised"

def open_chat():
    chatPage.lift()
    home["relief"] = "raised"
    myChatrooms["relief"] = "sunken"
    exercises["relief"] = "raised"
    help["relief"] = "raised"
    settings["relief"] = "raised"
    

def open_exercises():
    exercisePage.lift()
    home["relief"] = "raised"
    myChatrooms["relief"] = "raised"
    exercises["relief"] = "sunken"
    help["relief"] = "raised"
    settings["relief"] = "raised"

def open_settings():
    settingsPage.lift()
    home["relief"] = "raised"
    myChatrooms["relief"] = "raised"
    exercises["relief"] = "raised"
    help["relief"] = "raised"
    settings["relief"] = "sunken"

def open_help():
    helpPage.lift()
    home["relief"] = "raised"
    myChatrooms["relief"] = "raised"
    exercises["relief"] = "raised"
    help["relief"] = "sunken"
    settings["relief"] = "raised"

def open_reportForm():
    webbrowser.open("https://forms.gle/mqzgpgpWHABrVEjo7")


def getBaseLanguage(entry):
    getBaseLanguage.var = entry
    exercisesLabel["text"]="Which language do you want to practice?\nquelle langue voulez-vous pratiquer?\nque idioma quieres practicar\nChe lingua vuoi praticare?\n(en, fr, es, it)"
    getPracticeLanguageButton.lift()
    Answerbox.delete(0, "end")

def getPracticeLanguage(entry):
    getPracticeLanguage.var=entry
    exercisesLabel["text"]="Select dificulty\nsélectionner la difficulté\nSeleccione dificultad\nselezionare la difficoltà\n(easy, normal, hard)"
    getDifficultyButton.lift()
    Answerbox.delete(0, "end")


def getDifficulty(entry):
    getDifficulty.var=entry
    Answerbox.delete(0, "end")

    if getDifficulty.var == "easy":
        getDifficulty.xpval = 5
    if getDifficulty.var == "normal":
        getDifficulty.xpval = 10
    if getDifficulty.var == "hard":
        getDifficulty.xpval = 20
    submitButton.lift()
    questionButton["state"]="normal"


def getQuestion():
    translator = Translator()

    with open("WinterHack\\phrases.csv") as f:
        eyes = DictReader(f)
        matches = []

        for row in eyes:
            if row["difficulty"] == getDifficulty.var:
                matches.append(row)

    for i in range(4):
        exercise = choice(matches)
        matches.remove(exercise)
        type_ = randint(0, 1)
        if type_ == 0:
            question = translator.translate(exercise["question"], dest=getPracticeLanguage.var).text
            getQuestion.answer = translator.translate(exercise["question"], dest=getBaseLanguage.var).text
        else:
            question = translator.translate(exercise["question"], dest=getBaseLanguage.var).text
            getQuestion.answer = translator.translate(exercise["question"], dest=getPracticeLanguage.var).text
    exercisesLabel["text"]=question


def submitAnswer(entry):
    global exp
    if entry == getQuestion.answer:
        exp += getDifficulty.xpval
        feedbackLabel["text"] = f"Correct! {choice(['Nice work.', 'Excellent!', 'Good job!'])} Gained {getDifficulty.xpval} XP, for a total of {exp} XP! You'll fluently speak in no time!"
        global expText
        expText=tk.Label(recFrame, bg="white", text="Total XP: " + str(exp), font=("Cambria",16))
        expText.place(relx=0.1, rely=0.05, relwidth=0.2, relheight=0.2)

    if entry != getQuestion.answer:
        feedbackLabel["text"] = f"Incorrect! Don't worry, you still got this! The correct answer was {getQuestion.answer}"
    Answerbox.delete(0, "end")

#root is the main parent, holds everything basically
root = tk.Tk()

username="CosmiKolor"
lvl=20
firstQuestion = True





#Accuracy is calculated by taking the percentage of questions the user answered correctly within the past 50 exercises
acc=78
pfp=tk.PhotoImage(file="WinterHack\\defaultpfp.png")


#canvas is primarily for drawing shapes and things
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()


#main frames/blocks
sidebar=tk.Frame(root, bg="#c3d1fb")
sidebar.place(relx=0, rely=0, relwidth=0.2, relheight=1)

topbar=tk.Frame(root, bg="#6074FF")
topbar.place(relx=0, rely=0, relwidth=1, relheight=0.12)

mainFrame=tk.Frame(root, bg="#e8ebee")
mainFrame.place(relx=0.2, rely=0.12, relwidth=0.8, relheight=0.88)

#Pages
settingsPage = tk.Frame(mainFrame, bg="yellow")
settingsPage.place(relx=0, rely=0,  relheight=1, relwidth=1)

helpPage = tk.Frame(mainFrame, bg="#e8ebee")
helpPage.place(relx=0, rely=0,  relheight=1, relwidth=1)

chatPage = tk.Frame(mainFrame, bg="gray")
chatPage.place(relx=0, rely=0,  relheight=1, relwidth=1)

exercisePage = tk.Frame(mainFrame, bg="#e8ebee")
exercisePage.place(relx=0, rely=0,  relheight=1, relwidth=1)

homePage = tk.Frame(mainFrame, bg="#e8ebee")
homePage.place(relx=0, rely=0,  relheight=1, relwidth=1)

#Topbar Contents
reportBug=tk.Button(topbar, text="Report an Issue", anchor="w", font=("Cambria",13), fg="white", bg="#6074FF", borderwidth=0, command=open_reportForm)
reportBug.place(relx=0.88, rely=0.2, relwidth=0.1, relheight=0.6)

logo=tk.PhotoImage(file="WinterHack\\logo.png")
logoButton=tk.Button(topbar, image=logo, relief="groove", bg="#6074FF", bd="0")
logoButton.place(relx = 0, rely=0, relwidth=0.2, relheight=1)

#Sidebar Contents

pfp=tk.Label(sidebar, image=pfp, bg="white")
pfp.place(relx=0.2, rely=0.15, relwidth=0.6, relheight=0.2)

home = tk.Button(sidebar, text= "Home", background="#ebefff", font=("Cambria",12), activebackground="#e8ebee", relief="sunken", command=open_home)
home.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.05)

myChatrooms = tk.Button(sidebar, text= "My Chatrooms", background="#ebefff", font=("Cambria",12), activebackground="#e8ebee", command=open_chat)
myChatrooms.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.05)

exercises = tk.Button(sidebar, text= "Exercises", background="#ebefff", font=("Cambria",12), activebackground="#e8ebee", command=open_exercises)
exercises.place(relx=0.1, rely=0.6, relwidth=0.8, relheight=0.05)

help = tk.Button(sidebar, text= "Help", background="#ebefff", font=("Cambria",12), activebackground="#e8ebee", command=open_help)
help.place(relx=0.1, rely=0.7, relwidth=0.8, relheight=0.05)

settings = tk.Button(sidebar, text= "Settings", background="#ebefff", font=("Cambria",12), activebackground="#e8ebee", command=open_settings)
settings.place(relx=0.1, rely=0.8, relwidth=0.8, relheight=0.05)

#HOMEPAGE Mainframe contents

welcomeFrame=tk.Frame(homePage, bg="white", relief="ridge", borderwidth=2)
welcomeFrame.place(relx=0.05, rely=0.05, relwidth= 0.9, relheight=0.2)

welcome=tk.Label(welcomeFrame, text="Welcome, " + username + "!", font=("Cambria bold",36), anchor="w", padx=20, bg="white")
welcome.place(relx=0.02, rely=0.05, relwidth=0.96, relheight=0.9)

recFrame=tk.Frame(homePage, bg="white", relief="ridge", borderwidth=2)
recFrame.place(relx=0.05, rely=0.3, relwidth= 0.9, relheight=0.6)

expGraphic=tk.PhotoImage(file="WinterHack\\exp.png")
expPic=tk.Label(recFrame, bg="white", image=expGraphic)
expPic.place(relx=0.1, rely=0.2, relwidth=0.2, relheight=0.5)
expText=tk.Label(recFrame, bg="white", text="Total XP: " + str(exp), font=("Cambria",16))
expText.place(relx=0.1, rely=0.05, relwidth=0.2, relheight=0.2)
expInfo=tk.Label(recFrame, bg="white", text="Harder questions grant more xp!", font=("Cambria",8))
expInfo.place(relx=0.1, rely=0.68, relwidth=0.2, relheight=0.1)

lvlGraphic=tk.PhotoImage(file="WinterHack\\lvl.png")
lvlPic=tk.Label(recFrame, bg="white", image=lvlGraphic)
lvlPic.place(relx=0.4, rely=0.2, relwidth=0.2, relheight=0.5)
lvlText=tk.Label(recFrame, bg="white", text="Current LVL: " + str(lvl), font=("Cambria",16))
lvlText.place(relx=0.4, rely=0.05, relwidth=0.2, relheight=0.2)
lvlInfo=tk.Label(recFrame, bg="white", text="Complete exercises to level up!", font=("Cambria",8))
lvlInfo.place(relx=0.4, rely=0.68, relwidth=0.2, relheight=0.1)

accGraphic=tk.PhotoImage(file="WinterHack\\acc.png")
accPic=tk.Label(recFrame, bg="white", image=accGraphic)
accPic.place(relx=0.7, rely=0.2, relwidth=0.2, relheight=0.5)
accText=tk.Label(recFrame, bg="white", text="Exercise ACC: " + str(acc)+"%", font=("Cambria",16))
accText.place(relx=0.7, rely=0.05, relwidth=0.2, relheight=0.2)
accInfo=tk.Label(recFrame, bg="white", text="Based on the last 50 exercises!", font=("Cambria",8))
accInfo.place(relx=0.7, rely=0.68, relwidth=0.2, relheight=0.1)

exercisesButton=tk.Button(recFrame, bg="white", text="Begin Exercises", font=("Cambria",12), command=open_exercises)
exercisesButton.place(relx=0.1, rely=0.84, relwidth=0.38, relheight=0.1)

chatButton=tk.Button(recFrame, bg="white", text="Practice with a native speaker", font=("Cambria",12), command=open_chat)
chatButton.place(relx=0.52, rely=0.84, relwidth=0.38, relheight=0.1)

#HELPPAGE Mainframe contents

titleFrame=tk.Frame(helpPage, bg="white", relief="ridge", borderwidth=2)
titleFrame.place(relx=0.05, rely=0.05, relwidth= 0.9, relheight=0.28)
titleText=tk.Label(titleFrame, bg="white", text="New to WorldSpeak?", font=("Cambria bold",36), anchor="w", padx=20)
titleText.place(relx=0.02, rely=0, relwidth=0.96, relheight=0.85)
subtitleText=tk.Label(titleFrame, bg="white", text="We're here to help!", font=("Cambria bold",16), anchor="w", padx=20)
subtitleText.place(relx=0.02, rely=0.64, relwidth=0.96, relheight=0.15)

scrollFrame=tk.Frame(helpPage, bg="white", relief="ridge", borderwidth=2)
scrollFrame.place(relx=0.05, rely=0.38, relwidth= 0.9, relheight=0.52)

T = tk.Text(scrollFrame, font=("Cambria",12))
scroll = tk.Scrollbar(T)
scroll.pack(side=tk.RIGHT, fill=tk.Y)
T.place(relheight=0.9, relwidth=0.9, relx=0.05, rely=0.05)
scroll.config(command=T.yview)
T.config(yscrollcommand=scroll.set)
quote = """Welcome to WorldSpeak! This is an application designed to assist people in 
communicating with different world languages. It is a novel language
learning platform where users may complete exercises and practice 
speaking with a native speaker or someone else learning the language. 
Practice makes perfect!

 -> The navigation bar on the left is the main element of the 
    application. Click on the buttons to move around the site.

 -> To complete exercises, first select what language you speak, 
    and what language you would like to practice. Then, select 
    the difficulty of the exercises. Harder exercises grant more xp.

 -> Stay tuned for more updates! If you have a bug or a suggestion, 
    click on "report a bug" in the top left corner.

Thank you, and we hope you continue to use WorldSpeak!
"""
T.insert(tk.END, quote)
T.config(state="disabled")

#EXERCISES Mainframe Contents

headFrame=tk.Frame(exercisePage, bg="white", relief="ridge", borderwidth=2)
headFrame.place(relx=0.05, rely=0.05, relwidth= 0.9, relheight=0.2)
headText=tk.Label(headFrame, bg="white", text="Exercise Away!", font=("Cambria bold",36), anchor="w", padx=20)
headText.place(relx=0.02, rely=0.05, relwidth=0.96, relheight=0.9)

functionFrame=tk.Frame(exercisePage, bg="white", relief="ridge", borderwidth=2)
functionFrame.place(relx=0.05, rely=0.3, relwidth= 0.9, relheight=0.6)

exercisesLabel=tk.Label(functionFrame, font=("Cambria bold",16), bg="white", borderwidth=0, text="What language do you speak?\nQuelle langue parlez-vous?\nQué idioma hablas?\nChe lingua parli?\n(en, fr, es, it)", anchor="nw", justify="left")
exercisesLabel.place(relx=0.05, rely=0.1, relheight=0.4, relwidth=0.9)

feedbackLabel=tk.Label(functionFrame, font=("Cambria",12), bg="white", fg="red", borderwidth=0, text="your feedback will appear here!", anchor="nw", justify="left")
feedbackLabel.place(relx=0.05, rely=0.55, relheight=0.2, relwidth=0.9)

Answerbox = tk.Entry(functionFrame, font= ("Cambria",16))
Answerbox.place(relx=0.05, rely=0.7, relheight=0.2, relwidth=0.7)


questionButton=tk.Button(functionFrame, text="NEXT", font=("Cambria bold",16), bg="#ebefff", command=lambda: getQuestion(), state="disabled")
questionButton.place(relx=0.8, rely=0.4, relheight=0.2, relwidth=0.15)

submitButton=tk.Button(functionFrame, text="OK", font=("Cambria bold",16), bg="#ebefff", command=lambda: submitAnswer(Answerbox.get()))
submitButton.place(relx=0.8, rely=0.7, relheight=0.2, relwidth=0.15)

getDifficultyButton=tk.Button(functionFrame, text="OK", font=("Cambria bold",16), bg="#ebefff", command=lambda: getDifficulty(Answerbox.get()))
getDifficultyButton.place(relx=0.8, rely=0.7, relheight=0.2, relwidth=0.15)

getPracticeLanguageButton=tk.Button(functionFrame, text="OK", font=("Cambria bold",16), bg="#ebefff", command=lambda: getPracticeLanguage(Answerbox.get()))
getPracticeLanguageButton.place(relx=0.8, rely=0.7, relheight=0.2, relwidth=0.15)

getBaseLanguageButton=tk.Button(functionFrame, text="OK", font=("Cambria bold",16), bg="#ebefff", command=lambda: getBaseLanguage(Answerbox.get()))
getBaseLanguageButton.place(relx=0.8, rely=0.7, relheight=0.2, relwidth=0.15)


root.title("WorldSpeak")
root.update()
root.mainloop()
