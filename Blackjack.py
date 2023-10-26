# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 18:42:31 2023

@author: I_Henri

"""



from tkinter import *
import os
import random



class Player:
    def __init__(self):
        self.cards = []
        self.potMoney = 0
        self.isdealer = True
        self.money = 50
        self.hand = []
        self.cards_2 = []
        self.potMoney_2 = 0
        self.hand_2 = []
        
    def getAcard(self, deck):
        if len(deck) == 0:
            deck = os.listdir('./deck_p')
        self.hand.append(random.choice(deck))
        deck.remove(self.hand[len(self.hand)-1])
        
    def getAcard_2(self, deck):
        if len(deck) == 0:
            deck = os.listdir('./deck_p')
        self.hand_2.append(random.choice(deck))
        deck.remove(self.hand_2[len(self.hand_2)-1])
                
    def displayCards_2(self):
        self.cards_2.clear()
        for i in range(len(self.hand_2)):
            img_2 = PhotoImage(file='./deck_p/'+self.hand_2[i])
            self.cards_2.append(Label(window, image=img_2))
            self.cards_2[i].Photo = img_2
            self.cards_2[i].grid(column=i, row=7, padx=5)
            self.cards_2[i]['bg'] = '#01550a'
    
    def displayCards(self):
        self.cards.clear()
        if self.isdealer:
            for i in range(len(self.hand)):
                img = PhotoImage(file='./deck_p/'+self.hand[i])
                self.cards.append(Label(window, image=img))
                self.cards[i].Photo = img
                self.cards[i].grid(column=i, row=2, padx=5)
                self.cards[i]['bg'] = '#01550a'
        if not self.isdealer:
            for i in range(len(self.hand)):
                img = PhotoImage(file='./deck_p/'+self.hand[i])
                self.cards.append(Label(window, image=img))
                self.cards[i].Photo = img
                self.cards[i].grid(column=i, row=5, padx=5)
                self.cards[i]['bg'] = '#01550a'
    
    def handValue(self, i):
        value = 0
        if "two" in player.hand[i]:
            value = 2
        if "three" in player.hand[i]:
            value = 3
        if "four" in player.hand[i]:
            value = 4
        if "five" in player.hand[i]:
            value = 5
        if "six" in player.hand[i]:
            value = 6
        if "seven" in player.hand[i]:
            value = 7
        if "eight" in player.hand[i]:
            value = 8
        if "nine" in player.hand[i]:
            value = 9
        if "ten" in player.hand[i]:
            value = 10
        if "jack" in player.hand[i]:
            value = 10
        if "queen" in player.hand[i]:
            value = 10
        if "king" in player.hand[i]:
            value = 10
        if "ace" in player.hand[i]:
            value = 1
        return value
        
def newHand(newHandButton, startButton):
    newHandButton.grid_forget()
    if len(dealer.cards) != 0:
        for i in range(len(dealer.cards)):
            dealer.cards[i].grid_forget()
    if len(player.cards) != 0:
        for i in range(len(player.cards)):
            player.cards[i]['image'] = ""
            player.cards[i]['text'] = "  "
            player.cards[i]['font'] = 'roman 125 bold'
            player.cards[i]['fg'] = '#01550a'
            player.cards[i]['bg'] = '#01550a'
    if len(player.cards_2) != 0:
        for i in range(len(player.cards_2)):
            player.cards_2[i]['image'] = ""
            player.cards_2[i]['text'] = "  "
            player.cards_2[i]['font'] = 'roman 125 bold'
            player.cards_2[i]['fg'] = '#01550a'
            player.cards_2[i]['bg'] = '#01550a'
    
    startGame(startButton, player, dealer)

def reset(playerCardsLabel_2, potMoneyLabel_2):
    if player.hand_2 != 0:
        playerCardsLabel_2 = Label(window, text="Player Cards(split)  ", font='roman 16 bold', fg='#01550a', bg='#01550a')
        playerCardsLabel_2.grid(column=0, row=6)
        potMoneyLabel_2 = Label(window, text='Bet: '+str(player.potMoney_2), font='roman 16 bold', fg='#01550a', bg='#01550a')
        potMoneyLabel_2.grid(column=1, row=6)
    gameMsg.grid_forget()
    player.cards.clear()
    player.hand.clear()
    player.cards_2.clear()
    player.hand_2.clear()
    dealer.cards.clear()
    dealer.hand.clear()
        
def cleanButtons(doubleDownButton, hitButton, splitButton, standButton, doubleDownButton_2, hitButton_2, standButton_2):
    doubleDownButton.grid_forget()
    hitButton.grid_forget()
    splitButton.grid_forget()
    standButton.grid_forget()
    if len(player.hand_2) != 0:
        doubleDownButton_2.grid_forget()
        hitButton_2.grid_forget()
        standButton_2.grid_forget()
        
def showNewHandButton(startButton):
    newHandButton = Button(window, text='New Hand', font='roman 16 bold', fg='white', bg='grey')
    newHandButton.grid(column=3, row=4)
    newHandButton['command'] = lambda: newHand(newHandButton, startButton)

def blackjackMsg():
    gameMsg['text'] = 'Blackjack :)'
    gameMsg.grid(column=10, row=4)
    
def bustMsg_2():
    gameMsg_2['text'] = 'Bust :('
    gameMsg_2.grid(column=10, row=6)

def bustMsg():
    gameMsg['text'] = 'Bust :('
    gameMsg.grid(column=10, row=4)
    
def victoryMsg_2():
    gameMsg_2['text'] = 'Victory :)'
    gameMsg_2.grid(column=10, row=6)

def victoryMsg():
    gameMsg['text'] = 'Victory :)'
    gameMsg.grid(column=10, row=4)
    
def defeatMsg_2():
    gameMsg_2['text'] = 'Defeat :('
    gameMsg_2.grid(column=10, row=6)

def defeatMsg():
    gameMsg['text'] = 'Defeat :('
    gameMsg.grid(column=10, row=4)
    
def drawMsg_2():
    gameMsg_2['text'] = 'Draw *.*'
    gameMsg_2.grid(column=10, row=6)

def drawMsg():
    gameMsg['text'] = 'Draw *.*'
    gameMsg.grid(column=10, row=4)

def countPoints_2(user):
    totalPoints = 0
    for i in range(len(user.hand_2)):
        if "two" in user.hand_2[i]:
            totalPoints += 2
        if "three" in user.hand_2[i]:
            totalPoints += 3
        if "four" in user.hand_2[i]:
            totalPoints += 4
        if "five" in user.hand_2[i]:
            totalPoints += 5
        if "six" in user.hand_2[i]:
            totalPoints += 6
        if "seven" in user.hand_2[i]:
            totalPoints += 7
        if "eight" in user.hand_2[i]:
            totalPoints += 8
        if "nine" in user.hand_2[i]:
            totalPoints += 9
        if "ten" in user.hand_2[i]:
            totalPoints += 10
        if "jack" in user.hand_2[i]:
            totalPoints += 10
        if "queen" in user.hand_2[i]:
            totalPoints += 10
        if "king" in user.hand_2[i]:
            totalPoints += 10
    for i in range(len(user.hand_2)):
        if "ace" in user.hand_2[i]:
            if totalPoints < 11:
                totalPoints += 11
            else:
                totalPoints += 1
    return totalPoints

def countPoints(user):
    totalPoints = 0
    for i in range(len(user.hand)):
        if "two" in user.hand[i]:
            totalPoints += 2
        if "three" in user.hand[i]:
            totalPoints += 3
        if "four" in user.hand[i]:
            totalPoints += 4
        if "five" in user.hand[i]:
            totalPoints += 5
        if "six" in user.hand[i]:
            totalPoints += 6
        if "seven" in user.hand[i]:
            totalPoints += 7
        if "eight" in user.hand[i]:
            totalPoints += 8
        if "nine" in user.hand[i]:
            totalPoints += 9
        if "ten" in user.hand[i]:
            totalPoints += 10
        if "jack" in user.hand[i]:
            totalPoints += 10
        if "queen" in user.hand[i]:
            totalPoints += 10
        if "king" in user.hand[i]:
            totalPoints += 10
    for i in range(len(user.hand)):
        if "ace" in user.hand[i]:
            if totalPoints < 11:
                totalPoints += 11
            else:
                totalPoints += 1
    return totalPoints
    
def dealerInitialHand():
    card_1 = PhotoImage(file='./backside.png')
    card_2 = PhotoImage(file='./deck_p/'+dealer.hand[0])
    dealerCard_1 = Label(window, image=card_1)
    dealerCard_1.Photo = card_1
    dealerCard_1.grid(column=1, row=2)
    dealerCard_1['bg'] = '#01550a'
    dealerCard_2 = Label(window, image=card_2)
    dealerCard_2.Photo = card_2
    dealerCard_2.grid(column=0, row=2)
    dealerCard_2['bg'] = '#01550a'

def createLabels_2():
    playerCardsLabel_2 = Label(window, text="Player Cards(split)  ", font='roman 16 bold', fg='white', bg='#01550a')
    playerCardsLabel_2.grid(column=0, row=6)
    potMoneyLabel_2 = Label(window, text='Bet: '+str(player.potMoney_2), font='roman 16 bold', fg='#fee000', bg='#01550a')
    potMoneyLabel_2.grid(column=1, row=6)

def createLabels():
    dealersCardsLabel = Label(window, text="Dealer Cards", font='roman 16 bold', fg='white', bg='#01550a')
    dealersCardsLabel.grid(column=0, row=1)
    dealerCompraAte16 = Label(window, text="Dealer must stand on 17", font='roman 14 bold', fg='blue', bg='#01550a')
    dealerCompraAte16.grid(column=1, row=1)
    dealerParaNo17 = Label(window, text="and must draw to 16", font='roman 14 bold', fg='blue', bg='#01550a')
    dealerParaNo17.grid(column=2, row=1)
    playerCardsLabel = Label(window, text="Player Cards   ", font='roman 16 bold', fg='white', bg='#01550a')
    playerCardsLabel.grid(column=0, row=4)
    potMoneyLabel = Label(window, text='Bet: '+str(player.potMoney), font='roman 16 bold', fg='#fee000', bg='#01550a')
    potMoneyLabel.grid(column=1, row=4)
    playerMoney = Label(window, text='Money: '+str(player.money), font='roman 16 bold', fg='#fee000', bg='black')
    playerMoney.grid(column=9, row=4, padx=5)

def setWindow(window, player):
    window.title("BlackJack")
    window.state('zoomed')
    window['bg'] = '#01550a'
    startButton = Button(window, text='Start', font='roman 16 bold', fg='white', bg='grey')
    startButton['command'] = lambda: startGame(startButton, player, dealer)
    startButton.grid(column=1, row=3, padx= 650, pady=300)
    newHandButton = Button()
    
def doubleDown_2(startButton, doubleDownButton, hitButton, splitButton, standButton, doubleDownButton_2, hitButton_2, standButton_2):
    if len(player.hand_2) == 2:
        player.money -= player.potMoney_2
        player.potMoney_2 += player.potMoney_2
        createLabels_2()
        hit_2(doubleDownButton, hitButton, splitButton, standButton, doubleDownButton_2, hitButton_2, standButton_2)
        if countPoints_2(player) < 22:
            stand_2(doubleDownButton, hitButton, splitButton, standButton, doubleDownButton_2, hitButton_2, standButton_2)

def hit_2(doubleDownButton, hitButton, splitButton, standButton, doubleDownButton_2, hitButton_2, standButton_2):
    player.getAcard_2(deck)
    player.displayCards_2()
    if countPoints_2(player) > 21:
        bustMsg_2()
        cleanButtons(doubleDownButton, hitButton, splitButton, standButton, doubleDownButton_2, hitButton_2, standButton_2)
        doubleDownButton.grid(column=5, row=4)
        hitButton.grid(column=3, row=4)
        splitButton.grid(column=4, row=4)
        standButton.grid(column=2, row=4)
        
def stand_2(doubleDownButton, hitButton, splitButton, standButton, doubleDownButton_2, hitButton_2, standButton_2):
    cleanButtons(doubleDownButton, hitButton, splitButton, standButton, doubleDownButton_2, hitButton_2, standButton_2)
    doubleDownButton.grid(column=5, row=4)
    hitButton.grid(column=3, row=4)
    splitButton.grid(column=4, row=4)
    standButton.grid(column=2, row=4)

def split(startButton, doubleDownButton, hitButton, splitButton, standButton, doubleDownButton_2, hitButton_2, standButton_2):
    if len(player.hand_2) == 0:
        if len(player.hand) == 2:
            if player.handValue(0) == player.handValue(1):
                player.hand_2.append(player.hand[1])
                player.hand.pop()
                player.getAcard(deck)
                player.getAcard_2(deck)
                player.displayCards()
                player.displayCards_2()
                cleanButtons(doubleDownButton, hitButton, splitButton, standButton, doubleDownButton_2, hitButton_2, standButton_2)
                doubleDownButton_2 = Button(window, text='Double Down', font='roman 10', fg='white', bg='grey')
                doubleDownButton_2.grid(column=5, row=6, padx=5)
                doubleDownButton_2['command'] = lambda: doubleDown_2(startButton, doubleDownButton, hitButton, splitButton, standButton, doubleDownButton_2, hitButton_2, standButton_2)
                hitButton_2 = Button(window, text='Hit', font='roman 10', fg='white', bg='grey')
                hitButton_2.grid(column=3, row=6, padx=5)
                hitButton_2['command'] = lambda: hit_2(doubleDownButton, hitButton, splitButton, standButton, doubleDownButton_2, hitButton_2, standButton_2)
                standButton_2 = Button(window, text='Stand', font='roman 10', fg='white', bg='grey')
                standButton_2.grid(column=2, row=6)
                standButton_2['command'] = lambda: stand_2(doubleDownButton, hitButton, splitButton, standButton, doubleDownButton_2, hitButton_2, standButton_2)
                player.money = player.money - 1
                player.potMoney_2 = 1
                createLabels_2()
    
def doubleDown(startButton, doubleDownButton, hitButton, splitButton, standButton, doubleDownButton_2, hitButton_2, standButton_2):
    if len(player.hand) == 2:
        player.money -= player.potMoney
        player.potMoney += player.potMoney
        createLabels()
        hit(startButton, doubleDownButton, hitButton, splitButton, standButton, doubleDownButton_2, hitButton_2, standButton_2)
        if countPoints(player) < 22:
            stand(startButton, doubleDownButton, hitButton, splitButton, standButton,  doubleDownButton_2, hitButton_2, standButton_2)

def hit(startButton, doubleDownButton, hitButton, splitButton, standButton, doubleDownButton_2, hitButton_2, standButton_2):
    player.getAcard(deck)
    player.displayCards()
    if countPoints(player) > 21:
        if len(player.hand_2) != 0:
            if countPoints_2(player) < 22:
                while countPoints(dealer) < 17:
                    dealer.getAcard(deck)
                dealer.displayCards()
                if countPoints_2(player) < 22:
                    if len(player.hand_2) != 0:
                        if countPoints(dealer) < countPoints_2(player):
                            player.money += player.potMoney_2*2
                            victoryMsg_2()
                        if countPoints(dealer) > countPoints_2(player):
                            defeatMsg_2()
                        if countPoints(dealer) == countPoints_2(player):
                            drawMsg_2()
                            player.money += player.potMoney_2
        bustMsg()
        cleanButtons(doubleDownButton, hitButton, splitButton, standButton,  doubleDownButton_2, hitButton_2, standButton_2)
        showNewHandButton(startButton)
    
def stand(startButton, doubleDownButton, hitButton, splitButton, standButton, doubleDownButton_2, hitButton_2, standButton_2):
    while countPoints(dealer) < 17:
        dealer.getAcard(deck)
    dealer.displayCards()
    if countPoints(dealer) < 22:
        if countPoints_2(player) < 22:
            if len(player.hand_2) != 0:
                if countPoints(dealer) < countPoints_2(player):
                    player.money += player.potMoney_2*2
                    victoryMsg_2()
                if countPoints(dealer) > countPoints_2(player):
                    defeatMsg_2()
                if countPoints(dealer) == countPoints_2(player):
                    drawMsg_2()
                    player.money += player.potMoney_2
        if countPoints(dealer) < countPoints(player):
            player.money += player.potMoney*2
            victoryMsg()
            cleanButtons(doubleDownButton, hitButton, splitButton, standButton, doubleDownButton_2, hitButton_2, standButton_2)
            showNewHandButton(startButton)
        if countPoints(dealer) > countPoints(player):
            defeatMsg()
            cleanButtons(doubleDownButton, hitButton, splitButton, standButton, doubleDownButton_2, hitButton_2, standButton_2)
            showNewHandButton(startButton)
        if countPoints(dealer) == countPoints(player):
            drawMsg()
            player.money += player.potMoney
            cleanButtons(doubleDownButton, hitButton, splitButton, standButton, doubleDownButton_2, hitButton_2, standButton_2)
            showNewHandButton(startButton)
    else:
        if len(player.hand_2) != 0:
            if countPoints_2(player) < 22:
                player.money += player.potMoney_2
                victoryMsg_2()
        player.money += player.potMoney*2
        victoryMsg()
        cleanButtons(doubleDownButton, hitButton, splitButton, standButton, doubleDownButton_2, hitButton_2, standButton_2)
        showNewHandButton(startButton)
    
def startGame(startButton, player, dealer):
    gameMsg_2.grid_forget()
    doubleDownButton_2 = Button()
    hitButton_2 = Button()
    standButton_2 = Button()
    playerCardsLabel_2 = Label()
    potMoneyLabel_2 = Label()
    doubleDownButton = Button(window, text='Double Down', font='roman 10', fg='white', bg='grey')
    doubleDownButton.grid(column=5, row=4, padx=5)
    doubleDownButton['command'] = lambda: doubleDown(startButton, doubleDownButton, hitButton, splitButton, standButton, doubleDownButton_2, hitButton_2, standButton_2)
    hitButton = Button(window, text='Hit', font='roman 10', fg='white', bg='grey')
    hitButton.grid(column=3, row=4, padx=5)
    hitButton['command'] = lambda: hit(startButton, doubleDownButton, hitButton, splitButton, standButton, doubleDownButton_2, hitButton_2, standButton_2)
    splitButton = Button(window, text='Split', font='roman 10', fg='white', bg='grey')
    splitButton.grid(column=4, row=4)
    splitButton['command'] = lambda: split(startButton, doubleDownButton, hitButton, splitButton, standButton, doubleDownButton_2, hitButton_2, standButton_2)
    standButton = Button(window, text='Stand', font='roman 10', fg='white', bg='grey')
    standButton.grid(column=2, row=4)
    standButton['command'] = lambda: stand(startButton, doubleDownButton, hitButton, splitButton, standButton, doubleDownButton_2, hitButton_2, standButton_2)
    player.money = player.money - 1
    player.potMoney = 1
    player.potMoney_2 = 0
    startButton.grid_forget()
    reset(playerCardsLabel_2, potMoneyLabel_2)
    createLabels()
    for i in range(2):
        dealer.getAcard(deck)
        player.getAcard(deck)
    player.displayCards()
    dealerInitialHand()
    if countPoints(player) == 21:
        player.money += player.potMoney*2.5
        blackjackMsg()
        cleanButtons(doubleDownButton, hitButton, splitButton, standButton, doubleDownButton_2, hitButton_2, standButton_2)
        showNewHandButton(startButton)
    
window = Tk()
player = Player()
dealer = Player()
player.isdealer = False
gameMsg = Label(window, text='', font='roman 35 bold', fg='white', bg='#01550a')
gameMsg.grid(column=10, row=4)
gameMsg_2 = Label(window, text='BlackJack', font='roman 40 bold', fg='white', bg='#01550a')
gameMsg_2.grid(column=10, row=6)
setWindow(window, player)
deck = os.listdir('./deck_p')
window.mainloop()

