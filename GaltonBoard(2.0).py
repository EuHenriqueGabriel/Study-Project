# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 12:42:11 2023

@author: LuizH
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 10:05:38 2023

@author: I_Henri
"""

from tkinter import *
import numpy as np
import random
import matplotlib.pyplot as plt
from collections import Counter

def drop(frequency, n, balls, positions, k):
    for i in range(k):
        if i%(k*0.009) == 0:
            filteredFrequency, filteredPositions = frequencyCalculator(frequency, n, balls, positions)
            plot(filteredPositions, n, filteredFrequency)
        position = 0
        for _ in range(n):
            position += random.choice([-1,1])
        balls.append(position)

def frequencyCalculator(frequency, n, balls, positions):
    filteredFrequency = []
    filteredPositions = []
    for i in range((2*n)+1):
        frequency [i]= Counter(balls)[positions[i]]
    for i in range((2*n)+1):
        if frequency [i] != 0:
            filteredFrequency.append(frequency[i])
            filteredPositions.append(positions[i])
            
    return filteredFrequency, filteredPositions
    
def plot(positions, n, frequency):
    plt.plot(positions, frequency, 'o', color='black')
    plt.pause(0.00001)
    plt.show()
    
def boardSpin(rowsEntry, bolasEntry):
    balls = []
    n = int(rowsEntry.get())
    k = int(bolasEntry.get())
    frequency = np.zeros((2*n)+1)
    positions = np.zeros((2*n)+1) 
    for i in range((2*n)+1):
        positions[i] = i-n
    drop(frequency, n, balls, positions, k)

def main():
    root = Tk()
    root['bg'] = 'black'
    wikiText = Label(root, text='Esse programa simula um tabuleiro de Galton.\n\nO Tabuleiro de Galton, também conhecido como Quincunx, é um dispositivo inventado por Sir Francis Galton \npara demonstrar o teorema do limite central, em particular, que a distribuição normal é aproximada \nà distribuição binomial. Entre suas aplicações, oferecer ideias sobre regressão para média.\n\nO tabuleiro consiste de uma placa vertical com fileiras entrelaçadas de pinos. Bolas são jogadas a partir do topo; \nao bater nos pinos, elas se distribuem para a esquerda ou para a direita. Caso a probabilidade da bola ir para direita seja \nigual a probabilidade da bola ir para a esquerda, ao cair nas bandejas inferiores, a altura das bolas acumuladas nas \nbandejas, eventualmente, irá simular uma curva em forma de sino.\n', fg='white', bg='black', font='roman 12')
    wikiText.grid(column=0, row=0, columnspan=4)
    rows = Label(root, text="Digite o número de fileiras do tabuleiro: ", fg='white', bg='black', font='roman 14')
    rows.grid(column=0, row=1)
    bolas = Label(root, text="Digite o número de bolas a serem jogadas: ", fg='white', bg='black', font='roman 14')
    bolas.grid(column=2, row=1)
    rowsEntry = Entry(root, bd=3)
    rowsEntry.grid(column=1, row=1)
    bolasEntry = Entry(root, bd=3)
    bolasEntry.grid(column=3, row=1)
    button = Button(root, text='Drop', font='roman 14',height= 1, width=1, bd=6)
    button.grid(column=0, row=3, columnspan=4, sticky = W+E)
    button['command'] = lambda: boardSpin(rowsEntry, bolasEntry)
    img = PhotoImage(master=root, file='./Galton_box.png')
    boardImg = Label(root, image=img)
    boardImg.Photo = img
    boardImg.grid(column=0, row=2, columnspan=4, sticky=W+E)
    boardImg['bg'] = 'black'
    root.mainloop()
    
main()
    
