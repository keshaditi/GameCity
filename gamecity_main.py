import pygame
from tkinter import *
from PIL import ImageTk,Image
import Hangman as hg
import TTT as xo
import Color_game2 as cg


root =Tk()
root.geometry("612x386+100+100")
root.title("Games City")

def hang():
    import Hangman

def X():
    import TTT

def col():
    import colourGame
   cg.play()

canvas= Canvas(root,height=386,width=612)
image=ImageTk.PhotoImage(Image.open("gamecity.jpeg"))

canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()

lbl=Label(root,text="Games City",font=("Papyrus",40,"bold"))
lbl.place(x=180,y=50)

btn =Button(root,text= "Hangman",font=("Kristen ITC",15) ,command=hang,bg="#000000",fg="Orange")
btn.place(x=250, y= 160)

btn =Button(root,text= "Tic Tac Toe",font=("Kristen ITC",15),command=X,bg="#000000",fg="Orange")
btn.place(x=235, y= 240)

btn =Button(root,text= "ColorGame",font=("Kristen ITC",15),command=col,bg="#000000",fg="Orange")
btn.place(x=240, y= 320)

root.mainloop()