# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 15:42:16 2023

@author: LuizH
"""

from tkinter import *
from PIL import Image

class Animal:
    pass
    def __init__(self, x, y, ab):
        self.x = x
        self.y = y
        self.ab = ab
        self.canvas = Canvas(frame, width=100, height=100, highlightthickness=0)
        if self.ab == 'a':
            self.isDog = True
            self.dogImg = PhotoImage(file='./standdog.png')
            self.img = self.canvas.create_image(self.x, self.y, image=self.dogImg)
            self.canvas.tag_bind(self.img, '<B1-Motion>', self.move)
        else:
            self.isDog = False
            self.jaguarImg = PhotoImage(file='./standjaguar.png')
            self.img = self.canvas.create_image(self.x, self.y, image=self.jaguarImg)
            self.canvas.tag_bind(self.img, '<B1-Motion>', self.move)
        
    def move(self,e):
        if self.isDog:
            self.dogImg = PhotoImage(file='./standdog.png')
            #self.img = canvas.create_image(e.x, e.y, image=self.dogImg)
            e.widget.place(x=e.x_root, y=e.y_root,anchor=CENTER)
            #canvas.tag_bind(self.img, '<B1-Motion>', self.move)
        else:
            self.jaguarImg = PhotoImage(file='./standjaguar.png')
            #self.img = canvas.create_image(e.x, e.y, image=self.jaguarImg)
            e.widget.place(x=e.x_root, y=e.y_root,anchor=CENTER)
            #canvas.tag_bind(self.img, '<B1-Motion>', self.move)
             
def createWindowFrameAndCanvas():
    global root, frame, canvas
    root = Tk()
    root.state('zoomed')
    root['bg'] = 'black'
    frame = Frame(root)
    frame.pack()
    canvas = Canvas(frame, width=1300, height=710, highlightthickness=0)
    canvas['bg'] = 'black'
    canvas.pack()
    
def setBoardDogsJaguar(canvas, background):
    global dogs
    board = canvas.create_image(650, 355, image=background)
    dogs=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    xCoord = [224, 350, 472, 200, 331, 472, 169, 306, 155, 288, 446, 132, 272, 445]
    yCoord = [41, 39, 40, 172, 173, 174, 320, 325, 505, 505, 505, 650, 650, 650]
    for i in range(14):
        dogs[i] = Animal(xCoord[i],yCoord[i], 'a')
        dogs[i].canvas.tag_bind(dogs[i].img, '<B1-Motion>', dogs[i].move)
    jaguar = Animal(490, 298, 'b')

def main():
    createWindowFrameAndCanvas()
    background = PhotoImage(file='./board.png')
    setBoardDogsJaguar(canvas, background)
    root.mainloop()

main()