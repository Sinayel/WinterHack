from googletrans import Translator
from csv import DictReader
from random import randint, choice

baselanguage = input("Enter your language\nen\nfr\nsp\nit\nLanguage: ")
language = input("Enter the language to do exercises for\nen\nfr\nsp\nit\nLanguage: ")
difficulty = input("Enter the difficulty of the phrases \nEasy\nNormal\nHard\nDifficulty: ")

xptotal = 0
xpval = 0
if difficulty == "easy":
    xpval = 5
if difficulty == "normal":
    xpval = 10
if difficulty == "hard":
    xpval = 20
currentlevel = 0

translator = Translator()

with open("phrases.csv") as f:
    eyes = DictReader(f)
    matches = []

    for row in eyes:
        if row["difficulty"] == difficulty:
            matches.append(row)

for i in range(4):
    exercise = choice(matches)
    matches.remove(exercise)
    type_ = randint(0, 1)
    if type_ == 0:
        question = translator.translate(exercise["question"], dest=language).text
        answer = translator.translate(exercise["question"], dest=baselanguage).text
    else:
        question = translator.translate(exercise["question"], dest=baselanguage).text
        answer = translator.translate(exercise["question"], dest=language).text

    print(question)
    user = input()
    if user == answer:
        print(f"Correct! {choice(['Nice work.', 'Excellent!', 'Good job!'])}")
        xptotal += xpval
        print(f"Gained {xpval} XP, for a total of {xptotal} XP! You'll fluently speak in no time!")
    if user != answer:
        print(f"Incorrect! Don't worry, you still got this! The correct answer was {answer}")

print(f"You gained a total of {xptotal} XP! ", end="")

with open("xp.txt") as f:
    xp = int(f.read())
    xp += xptotal

with open("xp.txt", "w") as f:
    f.write(str(xp))

print(f"You are now level {xp // 15}!")
