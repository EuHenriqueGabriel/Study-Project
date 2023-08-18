# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 17:13:22 2023

@author: LuizH
"""

from tkinter import *


def mark(button, gameStatus, board, title_, playersScore):
    if title_['text'] == 'Turno: Jogador 1' or title_['text'] == 'Turno: Jogador 2':
        if button['text'] == ' ':
            if gameStatus.player == 1:
                button['text'] = "X"
                button['fg'] = 'blue'
                if checkWin(board, button):
                    title_['fg'] = 'green'
                    title_['text'] = 'JOGADOR 1 VENCEU'
                    gameStatus.p_1_score += 1 
                    playersScore[0]['text'] = "P-1: " + str(gameStatus.p_1_score)
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
                    gameStatus.p_2_score += 1 
                    playersScore[1]['text'] = "P-2: " + str(gameStatus.p_2_score)
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

def resetBoard(board, gameStatus, title_, resetButton):
    for i in range(9):
        board[i]['text'] = ' '
    gameStatus.player = 1
    title_['text'] = 'Turno: Jogador 1'
    resetButton['text'] = 'RESET'
    
class Status:
    def __init__(self):
        self.player = 1
        self.p_1_score = 0
        self.p_2_score = 0

def main():
    gameStatus = Status()
    janela = Tk()
    janela.title("TicTacToe")
    title_ = Label(janela, text= "TicTacToe", fg='white', bg='black')
    title_.grid(column=1, row=3, padx=10, pady=10)
    janela['bg'] = '#856ff8'
    
    button_1 = Button(janela, text=" ", fg='white', bg='white')
    button_1['command'] = lambda: mark(button_1, gameStatus, board, title_, playersScore)
    button_1.grid(column=0, row=2, padx=10, pady=10)
    button_2 = Button(janela, text=" ", fg='white', bg='white')
    button_2['command'] = lambda: mark(button_2, gameStatus, board, title_, playersScore)
    button_2.grid(column=1, row=2, padx=10, pady=10)
    button_3 = Button(janela, text=" ", fg='white', bg='white')
    button_3['command'] = lambda: mark(button_3, gameStatus, board, title_, playersScore)
    button_3.grid(column=2, row=2, padx=10, pady=10)
    button_4 = Button(janela, text=" ", fg='white', bg='white')
    button_4['command'] = lambda: mark(button_4, gameStatus, board, title_, playersScore)
    button_4.grid(column=0, row=1, padx=10, pady=10)
    button_5 = Button(janela, text=" ", fg='white', bg='white')
    button_5['command'] = lambda: mark(button_5, gameStatus, board, title_, playersScore)
    button_5.grid(column=1, row=1, padx=10, pady=10)
    button_6 = Button(janela, text=" ", fg='white', bg='white')
    button_6['command'] = lambda: mark(button_6, gameStatus, board, title_, playersScore)
    button_6.grid(column=2, row=1, padx=10, pady=10)
    button_7 = Button(janela, text=" ", fg='white', bg='white')
    button_7['command'] = lambda: mark(button_7, gameStatus, board, title_, playersScore)
    button_7.grid(column=0, row=0, padx=10, pady=10)
    button_8 = Button(janela, text=" ", fg='white', bg='white')
    button_8['command'] = lambda: mark(button_8, gameStatus, board, title_, playersScore)
    button_8.grid(column=1, row=0, padx=10, pady=10)
    button_9 = Button(janela, text=" ", fg='white', bg='white')
    button_9['command'] = lambda: mark(button_9, gameStatus, board, title_, playersScore)
    button_9.grid(column=2, row=0, padx=10, pady=10)
    
    board = [button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9]
    
    resetButton = Button(janela, text='PLAY')
    resetButton['command'] = lambda: resetBoard(board, gameStatus, title_, resetButton)
    resetButton.grid(column=1, row=4, padx=10, pady=10)
    
    playersScore = [Label(janela, text= "P-1: " + str(gameStatus.p_1_score), fg='white', bg='black'), Label(janela, text= "P-2: " + str(gameStatus.p_2_score), fg='white', bg='black')]
    playersScore[0].grid(column=0, row=4, padx=10, pady=10)
    playersScore[1].grid(column=2, row=4, padx=10, pady=10)
    janela.mainloop()
    
    
main()