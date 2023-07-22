import tkinter as Tk
from tkinter import *
from PIL import Image, ImageTk
import winsound
#Criar uma biblioteca de som

soundLibrary = {
    "CancelSound": "sounds\cancel.wav",
    "Door": "sounds\door.wav",
    "Femea": "sounds\emea.wav",
    "Spike": "sounds\plantada.wav"
    }

Window = Tk()
Window.geometry("600x800")
Window.resizable(False, False)
Window.configure(bg = "#2b2b2b")
Window.title("Soundboard")

def Create_Window():
    #logo
    photo = Image.open("Images/logo.png").resize((300, 100))
    logophoto = ImageTk.PhotoImage(photo, Image)
    Window.iconphoto(True, logophoto)

    #Imagem Botao
    SoundBoardButtonImage = ImageTk.PhotoImage(file = "Images/botao.png")
    # elinar garbage collection
    buttonlbl = Label(image = SoundBoardButtonImage)
    buttonlbl.image = SoundBoardButtonImage

    # Botao do soundboard
    soundButton1 = Button(Window, text = "Cancel", image = SoundBoardButtonImage, compound = "center", height = 200, width = 150, background = "#000000", relief = "solid", activebackground = "#000000", command = lambda: playSound(soundLibrary["CancelSound"]))
    soundButton1.grid( row = 1, column = 1, padx = 20, pady = 20, sticky = "we")

    soundButton2 = Button(Window, text = "Femea", image = SoundBoardButtonImage, compound = "center", height = 200, width = 150, background = "#000000", relief = "solid", activebackground = "#000000", command = lambda: playSound(soundLibrary["Femea"]))
    soundButton2.grid( row = 1, column = 2, padx = 20, pady = 20, sticky = "we")

    soundButton3 = Button(Window, text = "Door", image = SoundBoardButtonImage, compound = "center", height = 200, width = 150, background = "#000000", relief = "solid", activebackground = "#000000", command = lambda: playSound(soundLibrary["Door"]))
    soundButton3.grid( row = 1, column = 3, padx = 20, pady = 20, sticky = "we")

    soundButton4 = Button(Window, text = "Door", image = SoundBoardButtonImage, compound = "center", height = 200, width = 150, background = "#000000", relief = "solid", activebackground = "#000000", command = lambda: playSound(soundLibrary["Door"]))
    soundButton4.grid( row = 2, column = 1, padx = 20, pady = 20, sticky = "we")

    soundButton5 = Button(Window, text = "Door", image = SoundBoardButtonImage, compound = "center", height = 200, width = 150, background = "#000000", relief = "solid", activebackground = "#000000", command = lambda: playSound(soundLibrary["Door"]))
    soundButton5.grid( row = 2, column = 2, padx = 20, pady = 20, sticky = "we")

    soundButton6 = Button(Window, text = "Door", image = SoundBoardButtonImage, compound = "center", height = 200, width = 150, background = "#000000", relief = "solid", activebackground = "#000000", command = lambda: playSound(soundLibrary["Door"]))
    soundButton6.grid( row = 2, column = 3, padx = 20, pady = 20, sticky = "we")

    soundButton7 = Button(Window, text = "Door", image = SoundBoardButtonImage, compound = "center", height = 200, width = 150, background = "#000000", relief = "solid", activebackground = "#000000", command = lambda: playSound(soundLibrary["Door"]))
    soundButton7.grid( row = 3, column = 1, padx = 20, pady = 20, sticky = "we")

    soundButton8 = Button(Window, text = "Door", image = SoundBoardButtonImage, compound = "center", height = 200, width = 150, background = "#000000", relief = "solid", activebackground = "#000000", command = lambda: playSound(soundLibrary["Door"]))
    soundButton8.grid( row = 3, column = 2, padx = 20, pady = 20, sticky = "we")

    soundButton9 = Button(Window, text = "Spike Plant", image = SoundBoardButtonImage, compound = "center", height = 200, width = 150, background = "#000000", relief = "solid", activebackground = "#000000", command = lambda: playSound(soundLibrary["Spike"]))
    soundButton9.grid( row = 3, column = 3, padx = 20, pady = 20, sticky = "we")
# função toca o som selecionado
def playSound(sound):
    return winsound.PlaySound(sound, winsound.SND_ASYNC + winsound.SND_FILENAME)

Create_Window()

#Criar Window
Window.mainloop()
