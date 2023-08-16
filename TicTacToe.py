# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 17:13:22 2023

@author: LuizH
"""

from tkinter import *


def mark(button, gameStatus, board, title_):
    if button['text'] == ' ':
        if gameStatus.player == 1:
            button['text'] = "X"
            button['fg'] = 'blue'
            if checkWin(board, button):
                title_['fg'] = 'green'
                title_['text'] = 'JOGADOR 1 VENCEU'
            elif checkDraw(board):
                title_['text'] = 'EMPATE'
            else:
                title_['text'] = 'Turno: Jogador 2'
            gameStatus.player = 2
        else:
            button['text'] = "O"
            button['fg'] = 'red'
            if checkWin(board, button):
                title_['fg'] = 'green'
                title_['text'] = 'JOGADOR 2 VENCEU'
            elif checkDraw(board):
                title_['text'] = 'EMPATE'
            else:
                title_['text'] = 'Turno: Jogador 1'
            gameStatus.player = 1
        
def checkWin(board, button):
    quadradoMagico = [4,3,8,9,5,1,2,7,6]
    for x in range(9):
        for y in range(9):
            for z in range(9):
                if x != y and y != z and z != x:
                    if board[x]['text'] == button['text'] and board[y]['text'] == button['text'] and board[z]['text'] == button['text']:
                        if quadradoMagico[x] + quadradoMagico[y] + quadradoMagico[z] == 15:
                            return True
                    
def checkDraw(board):
    for i in range(9):
        if board[i]['text'] == ' ':
            return False
    return True

def resetBoard(board, gameStatus, title_):
    for i in range(9):
        board[i]['text'] = ' '
    gameStatus.player = 1
    title_['text'] = 'Turno: Jogador 1'
class Status:
    def __init__(self, player):
        self.player = 1

def main():
    gameStatus = Status(1)
    janela = Tk()
    janela.title("TicTacToe")
    title_ = Label(janela, text= "TicTacToe", fg='white', bg='black')
    title_.grid(column=1, row=3, padx=10, pady=10)
    janela['bg'] = '#856ff8'
    
    button_1 = Button(janela, text=" ", fg='white', bg='white')
    button_1['command'] = lambda: mark(button_1, gameStatus, board, title_)
    button_1.grid(column=0, row=2, padx=10, pady=10)
    button_2 = Button(janela, text=" ", fg='white', bg='white')
    button_2['command'] = lambda: mark(button_2, gameStatus, board, title_)
    button_2.grid(column=1, row=2, padx=10, pady=10)
    button_3 = Button(janela, text=" ", fg='white', bg='white')
    button_3['command'] = lambda: mark(button_3, gameStatus, board, title_)
    button_3.grid(column=2, row=2, padx=10, pady=10)
    button_4 = Button(janela, text=" ", fg='white', bg='white')
    button_4['command'] = lambda: mark(button_4, gameStatus, board, title_)
    button_4.grid(column=0, row=1, padx=10, pady=10)
    button_5 = Button(janela, text=" ", fg='white', bg='white')
    button_5['command'] = lambda: mark(button_5, gameStatus, board, title_)
    button_5.grid(column=1, row=1, padx=10, pady=10)
    button_6 = Button(janela, text=" ", fg='white', bg='white')
    button_6['command'] = lambda: mark(button_6, gameStatus, board, title_)
    button_6.grid(column=2, row=1, padx=10, pady=10)
    button_7 = Button(janela, text=" ", fg='white', bg='white')
    button_7['command'] = lambda: mark(button_7, gameStatus, board, title_)
    button_7.grid(column=0, row=0, padx=10, pady=10)
    button_8 = Button(janela, text=" ", fg='white', bg='white')
    button_8['command'] = lambda: mark(button_8, gameStatus, board, title_)
    button_8.grid(column=1, row=0, padx=10, pady=10)
    button_9 = Button(janela, text=" ", fg='white', bg='white')
    button_9['command'] = lambda: mark(button_9, gameStatus, board, title_)
    button_9.grid(column=2, row=0, padx=10, pady=10)
    
    board = [button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9]
    
    resetButton = Button(janela, text='RESET', command = lambda: resetBoard(board, gameStatus, title_) )
    resetButton.grid(column=1, row=4, padx=10, pady=10)
    janela.mainloop()
    
    
main()