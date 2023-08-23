import tkinter
from tkinter import *
import random
import winsound

game = Tk()
game.title("GLHF!")
sheet = Canvas(game, width=550, height=500, bg="gray")
sheet1 = Canvas(game, width=550, height=50, bg="white")
sheet2 = Canvas(game, width=100, height=200, bg="gray")
sheet.create_rectangle(300, 400, 50, 410, fill="goldenrod4")  # base for post
sheet.create_rectangle(50, 400, 70, 50, fill="goldenrod4")  # poleup for post
sheet.create_rectangle(50, 50, 200, 60, fill="goldenrod4")  # crossbeam for post
sheet.create_rectangle(195, 50, 200, 100, fill="goldenrod4")  # rope for post
AmountOfFails = 0
word_list = ("highway", "poor", "bend", "product", "layout", "subway", "calf", "deputy",
             "smoke", "banana", "buy", "faith", "pioneer", "carry", "warrant", "abridge",
             "joke", "troll", "summer", "lover", "infect", "attract", "zap", "state",
             "twist", "moist", "onion", "thick", "permanent", "villain", "curtain", "snow", "quirk")
choice = random.choice(word_list)
choice = choice.lower()
wordarray = list(choice)
guessedarray = list()
guess = Entry(game)
guess.lower()
guess.grid(row=0, column=0)


def failersMethod(AmountOfFails): # called by clicked counts fails and Displays
    global IncorrectGuesses
    IncorrectGuesses = AmountOfFails
    if IncorrectGuesses == 0:
        x = 0
    elif IncorrectGuesses == 1:
        sheet.create_oval(172, 150, 222, 100, fill="red")  # Head
    elif IncorrectGuesses == 2:
        sheet.create_rectangle(187, 150, 207, 250, fill="red")  # Body
    elif IncorrectGuesses == 3:
        sheet.create_polygon(130, 225, 120, 220, 187, 175, 187, 187, fill="red")  # Arm 1
    elif IncorrectGuesses == 4:
        sheet.create_polygon(255, 225, 265, 220, 207, 175, 207, 187, fill="red")  # Arm 2
    elif IncorrectGuesses == 5:
        sheet.create_polygon(197, 250, 187, 250, 167, 300, 177, 300, fill="red")  # leg 1
    elif IncorrectGuesses == 6:
        sheet.create_polygon(207, 250, 197, 250, 207, 300, 217, 300, fill="red")  # leg 2
    else:  # fail case/ need a break and quits
        print("fail")


def open():  # Called by Button, Creates game Frame, Gets word
    buttonforguessing = Button(game, text="Guess", command=clicked)
    buttonforguessing.grid(row=0, column=1)
    buttonforquitters = Button(game, text="I quit", command=game.destroy)
    buttonforquitters.grid(row=4, column=0)
    sheet.grid(row=2, column=0)
    sheet1.grid(row=3, column=0)
    sheet2.grid(row=2, column=1)
    lengthofword = (len(choice))
    x1 = 0
    x2 = 50
    y1 = 50
    y2 = 45
    for x in range(lengthofword):
        createTextAtX = (x2 + x1) / 2
        if choice[x] == ' ':
            sheet1.create_text(createTextAtX, 20, text=wordarray[x], fill="black", font='Helvetica 15 bold')
        elif choice[x] == '-':
            sheet1.create_text(createTextAtX, 20, text=wordarray[x], fill="black", font='Helvetica 15 bold')
        else:
            sheet1.create_rectangle(x1, y1, x2, y2, fill="black")
        x1 += 55
        x2 += 55
    failersMethod(0)


def clicked():  # When Guess Button is pressed this is called
    global AmountOfFails
    global wordarray
    x11 = 0
    x22 = 50
    y1 = 50
    y2 = 45
    guessed = guess.get()
    guessed.lower()
    if guessed.lower() in wordarray:
        for x in range(len(wordarray)):
            x3=x
            if wordarray[x] == guessed.lower():
                FillText = ((x3 *108) +55) / 2
                sheet1.create_rectangle(x11, y1, x22, y2, fill="black")
                sheet1.create_text(FillText, 20, text=wordarray[x], fill="black", font='Helvetica 15 bold')
                x11 += 55
                x22 += 55
    else:
        if guessed.lower() in guessedarray:
            # sound effect for fail
            winsound.PlaySound('mixkit-video-game-mystery-alert-234(1).wav', winsound.SND_FILENAME)
            x = 0
        else:
            i = AmountOfFails
            guessedarray.append(guessed.lower())  # this is creating a list that we are going to display,
            list1 = tkinter.StringVar(value=guessedarray)
            lst = tkinter.Listbox(sheet2, listvariable=list1, bg="gray")
            lst.grid(row=1, column=2)
            lstlabel = Label(sheet2, text="Incorrect letters", bg="gray").grid(row=0, column=2)
            AmountOfFails = AmountOfFails + 1
    failersMethod(AmountOfFails)




if __name__ == "__main__":
    root = Tk()
    root.geometry('200x200')
    Button1 = Button(root, text="New Game", fg="red", command=open)
    Button1.pack()
    mainloop()
