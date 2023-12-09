# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 00:11:50 2023

@author: LuizH
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 18:42:31 2023

@author: I_Henri

"""



from tkinter import *
import os
import random
import pyodbc

class Player:
    def __init__(self):
        self.id = 0
        self.cards = []
        self.potMoney = 0
        self.isdealer = True
        self.money = 0
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
            img_2 = PhotoImage(master=window, file='./deck_p/'+self.hand_2[i])
            self.cards_2.append(Label(window, image=img_2))
            self.cards_2[i].Photo = img_2
            self.cards_2[i].grid(column=i, row=7, padx=5)
            self.cards_2[i]['bg'] = '#01550a'
    
    def displayCards(self):
        self.cards.clear()
        if self.isdealer:
            for i in range(len(self.hand)):
                img = PhotoImage(master=window, file='./deck_p/'+self.hand[i])
                self.cards.append(Label(window, image=img))
                self.cards[i].Photo = img
                self.cards[i].grid(column=i, row=2, padx=5)
                self.cards[i]['bg'] = '#01550a'
        if not self.isdealer:
            for i in range(len(self.hand)):
                img = PhotoImage(master=window, file='./deck_p/'+self.hand[i])
                self.cards.append(Label(window))
                self.cards[i]['image'] = img
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
    
def connectDB():
    global cursor
    driver='{MySQL ODBC 8.2 ANSI Driver}'
    server='localhost'
    database='Blackjack'
    username='root'
    password=''
    conn = pyodbc.connect(Driver=driver,Server=server,Database=database,Uid=username,Pwd=password)
    cursor = conn.cursor()
    
def updateChips():
    command = f""" update Players
                   set Chips = {player.money}
                   where username='{username}'"""
    cursor.execute(command)

def signIn(UserNameEntry, PasswordEntry, signInButton):
    global username, signInLabel, registrationLabel
    registrationLabel = Label(window, text='', fg='#01550a', bg='#01550a' )
    registrationLabel.grid(column=2, row=7, padx=5)
    signInLabel = Label(window, text='', fg='#01550a', bg='#01550a' )
    signInLabel.grid(column=4, row=6, padx=5)
    username = UserNameEntry.get()
    password = PasswordEntry.get()
    if len(username) == 0 or username == '':
        signInLabel = Label(window, text='Invalid Username!', fg='red', bg='#01550a' )
        signInLabel.grid(column=4, row=6, padx=5)
        signInLabel.after(3000, signInLabel.destroy)
    elif len(password) == 0:
        signInLabel = Label(window, text='Invalid Password!', fg='red', bg='#01550a' )
        signInLabel.grid(column=4, row=6, padx=5)
        signInLabel.after(3000, signInLabel.destroy)
    else:
        command = f""" select Username, Password, Chips
                       from Players
                       where username='{username}'"""
        cursor.execute(command)
        playerInfo = cursor.fetchone()
        if playerInfo == None or playerInfo[1] != password:
            signInLabel = Label(window, text= str(username)+' is not registered!/Wrong password ', fg='red', bg='#01550a' )
            signInLabel.grid(column=4, row=6, padx=5)
            signInLabel.after(3000, signInLabel.destroy)
        else:
            player.money = playerInfo[2]
            startGame()
    

def register(newUserNameEntry, newPasswordEntry, confirmPasswordEntry):
    global registrationLabel
    username = newUserNameEntry.get()
    password = newPasswordEntry.get()
    confirmPassword = confirmPasswordEntry.get()
    chips = 100
    if len(username) == 0 or username == '':
        registrationLabel = Label(window, text='Invalid Username! ', fg='red', bg='#01550a' )
        registrationLabel.grid(column=2, row=7, padx=5)
        registrationLabel.after(3000, registrationLabel.destroy)
    elif len(password) == 0:
        registrationLabel = Label(window, text='Invalid Password! ', fg='red', bg='#01550a' )
        registrationLabel.grid(column=2, row=7, padx=5)
        registrationLabel.after(3000, registrationLabel.destroy)
    else:
        if password == confirmPassword:
            command = f""" insert into Players(Username, Password, Chips)
                            values('{username}', '{password}', {chips})"""
            try:
                cursor.execute(command)
                registrationLabel = Label(window, text='     Successfully registered!     '+u'\u2713', fg='#00e9d7', bg='#01550a' )
                registrationLabel.grid(column=2, row=7, padx=5)
                registrationLabel.after(3000, registrationLabel.destroy)
            except:
                registrationLabel = Label(window, text='This Username is already taken!', fg='red', bg='#01550a' )
                registrationLabel.grid(column=2, row=7)
                registrationLabel.after(3000, registrationLabel.destroy)
        else:
            registrationLabel = Label(window, text='        Passwords dont match!       ', fg='red', bg='#01550a' )
            registrationLabel.grid(column=2, row=7, padx=15)
            registrationLabel.after(3000, registrationLabel.destroy)
    
def close():
    global window, player, dealer, gameMsg, gameMsg_2, deck
    updateChips()
    window.destroy()
    window = Tk()
    player = Player()
    dealer = Player()
    player.isdealer = False
    connectDB()
    gameMsg = Label(window, text='', font='roman 35 bold', fg='white', bg='#01550a')
    gameMsg.grid(column=10, row=4)
    gameMsg_2 = Label(window, text='BlackJack', font='roman 40 bold', fg='white', bg='#01550a')
    gameMsg_2.grid(column=2, row=9, columnspan=2)
    setWindow(window, player)
    deck = os.listdir('./deck_p')
    window.mainloop()
        
def newHand(newHandButton, signInButton):
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
    
    startGame()

def reset(playerCardsLabel_2, potMoneyLabel_2):
    '''registrationLabel.destroy()
    signInLabel.destroy()'''
    blankText.grid_forget()
    createAccountText.grid_forget()
    signInText.grid_forget()
    newUserNameText.grid_forget()
    newPasswordText.grid_forget()
    confirmPasswordText.grid_forget()
    UserNameText.grid_forget()
    PasswordText.grid_forget()
    newUserNameEntry.grid_forget()
    newPasswordEntry .grid_forget()
    confirmPasswordEntry.grid_forget()
    UserNameEntry.grid_forget()
    PasswordEntry.grid_forget()
    registerButton.grid_forget()
    signInButton.grid_forget()
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
        
def showNewHandButton(signInButton):
    newHandButton = Button(window, text='New Hand', font='roman 16 bold', fg='white', bg='grey')
    newHandButton.grid(column=3, row=4)
    newHandButton['command'] = lambda: newHand(newHandButton, signInButton)

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
    card_1 = PhotoImage(master=window, file='./backside.png')
    card_2 = PhotoImage(master=window, file='./deck_p/'+dealer.hand[0])
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
    playerMoney = Label(window, text=str(username)+" - Chips: "+str(player.money), font='roman 16 bold', fg='#fee000', bg='black')
    playerMoney.grid(column=9, row=4, padx=5)

def setWindow(window, player):
    global createAccountText, signInText, newUserNameText, newPasswordText, confirmPasswordText, UserNameText, PasswordText, newUserNameEntry, newPasswordEntry, confirmPasswordEntry, UserNameEntry, PasswordEntry, registerButton, signInButton, blankText
    window.title("BlackJack")
    window.state('zoomed')
    window['bg'] = '#01550a'
    blankText = Label(window, text=' ', font='roman 16 bold', fg='#01550a', bg='#01550a')
    blankText.grid(column=0, row=0, padx= 150, pady=70)
    createAccountText = Label(window, text='Create Account', font='roman 16 bold', fg='white', bg='#01550a')
    createAccountText.grid(column=1, row=3, padx= 10, pady=10, columnspan=2)
    signInText = Label(window, text='Sign In', font='roman 16 bold', fg='white', bg='#01550a')
    signInText.grid(column=3, row=3, padx= 10, pady=10, columnspan=2)
    newUserNameText = Label(window, text='New Username', font='roman 16 bold', fg='white', bg='#01550a')
    newUserNameText.grid(column=1, row=4, padx= 0, pady=10)
    newPasswordText = Label(window, text='New Password', font='roman 16 bold', fg='white', bg='#01550a')
    newPasswordText.grid(column=1, row=5, padx= 0, pady=10)
    confirmPasswordText = Label(window, text='Confirm Password', font='roman 16 bold', fg='white', bg='#01550a')
    confirmPasswordText.grid(column=1, row=6, padx= 0, pady=10)
    UserNameText = Label(window, text='Username', font='roman 16 bold', fg='white', bg='#01550a')
    UserNameText.grid(column=3, row=4, padx= 10, pady=10)
    PasswordText = Label(window, text='Password', font='roman 16 bold', fg='white', bg='#01550a')
    PasswordText.grid(column=3, row=5, padx= 10, pady=10)
    newUserNameEntry = Entry(window, bd=3)
    newUserNameEntry.grid(column=2, row=4, padx= 0, pady=10)
    newPasswordEntry = Entry(window, bd=3, show='*')
    newPasswordEntry.grid(column=2, row=5, padx= 0, pady=10)
    confirmPasswordEntry = Entry(window, bd=3, show='*')
    confirmPasswordEntry.grid(column=2, row=6, padx= 10, pady=10)
    UserNameEntry = Entry(window, bd=3)
    UserNameEntry.grid(column=4, row=4, padx= 10, pady=10)
    PasswordEntry = Entry(window, bd=3, show='*')
    PasswordEntry.grid(column=4, row=5, padx= 10, pady=10)
    registerButton = Button(window, text='Register', font='roman 16 bold', fg='white', bg='grey' )
    registerButton['command'] = lambda: register(newUserNameEntry, newPasswordEntry, confirmPasswordEntry)
    registerButton.grid(column=2, row=8, padx= 10, pady=10)
    signInButton = Button(window, text='Enter', font='roman 16 bold', fg='white', bg='grey' )
    signInButton['command'] = lambda: signIn(UserNameEntry, PasswordEntry, signInButton)
    signInButton.grid(column=4, row=7, padx=10, pady=10)
    newHandButton = Button()
    
def doubleDown_2(signInButton, doubleDownButton, hitButton, splitButton, standButton, doubleDownButton_2, hitButton_2, standButton_2):
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

def split(signInButton, doubleDownButton, hitButton, splitButton, standButton, doubleDownButton_2, hitButton_2, standButton_2):
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
                doubleDownButton_2['command'] = lambda: doubleDown_2(signInButton, doubleDownButton, hitButton, splitButton, standButton, doubleDownButton_2, hitButton_2, standButton_2)
                hitButton_2 = Button(window, text='Hit', font='roman 10', fg='white', bg='grey')
                hitButton_2.grid(column=3, row=6, padx=5)
                hitButton_2['command'] = lambda: hit_2(doubleDownButton, hitButton, splitButton, standButton, doubleDownButton_2, hitButton_2, standButton_2)
                standButton_2 = Button(window, text='Stand', font='roman 10', fg='white', bg='grey')
                standButton_2.grid(column=2, row=6)
                standButton_2['command'] = lambda: stand_2(doubleDownButton, hitButton, splitButton, standButton, doubleDownButton_2, hitButton_2, standButton_2)
                player.money = player.money - 1
                player.potMoney_2 = 1
                createLabels_2()
    
def doubleDown(signInButton, doubleDownButton, hitButton, splitButton, standButton, doubleDownButton_2, hitButton_2, standButton_2):
    if len(player.hand) == 2:
        player.money -= player.potMoney
        player.potMoney += player.potMoney
        createLabels()
        hit(signInButton, doubleDownButton, hitButton, splitButton, standButton, doubleDownButton_2, hitButton_2, standButton_2)
        if countPoints(player) < 22:
            stand(signInButton, doubleDownButton, hitButton, splitButton, standButton,  doubleDownButton_2, hitButton_2, standButton_2)

def hit(signInButton, doubleDownButton, hitButton, splitButton, standButton, doubleDownButton_2, hitButton_2, standButton_2):
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
        showNewHandButton(signInButton)
    
def stand(signInButton, doubleDownButton, hitButton, splitButton, standButton, doubleDownButton_2, hitButton_2, standButton_2):
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
            showNewHandButton(signInButton)
        if countPoints(dealer) > countPoints(player):
            defeatMsg()
            cleanButtons(doubleDownButton, hitButton, splitButton, standButton, doubleDownButton_2, hitButton_2, standButton_2)
            showNewHandButton(signInButton)
        if countPoints(dealer) == countPoints(player):
            drawMsg()
            player.money += player.potMoney
            cleanButtons(doubleDownButton, hitButton, splitButton, standButton, doubleDownButton_2, hitButton_2, standButton_2)
            showNewHandButton(signInButton)
    else:
        if len(player.hand_2) != 0:
            if countPoints_2(player) < 22:
                player.money += player.potMoney_2
                victoryMsg_2()
        player.money += player.potMoney*2
        victoryMsg()
        cleanButtons(doubleDownButton, hitButton, splitButton, standButton, doubleDownButton_2, hitButton_2, standButton_2)
        showNewHandButton(signInButton)
    
def startGame():
    updateChips()
    gameMsg_2.grid_forget()
    doubleDownButton_2 = Button()
    hitButton_2 = Button()
    standButton_2 = Button()
    playerCardsLabel_2 = Label()
    potMoneyLabel_2 = Label()
    doubleDownButton = Button(window, text='Double Down', font='roman 10', fg='white', bg='grey')
    doubleDownButton.grid(column=5, row=4, padx=5)
    doubleDownButton['command'] = lambda: doubleDown(signInButton, doubleDownButton, hitButton, splitButton, standButton, doubleDownButton_2, hitButton_2, standButton_2)
    hitButton = Button(window, text='Hit', font='roman 10', fg='white', bg='grey')
    hitButton.grid(column=3, row=4, padx=5)
    hitButton['command'] = lambda: hit(signInButton, doubleDownButton, hitButton, splitButton, standButton, doubleDownButton_2, hitButton_2, standButton_2)
    splitButton = Button(window, text='Split', font='roman 10', fg='white', bg='grey')
    splitButton.grid(column=4, row=4)
    splitButton['command'] = lambda: split(signInButton, doubleDownButton, hitButton, splitButton, standButton, doubleDownButton_2, hitButton_2, standButton_2)
    standButton = Button(window, text='Stand', font='roman 10', fg='white', bg='grey')
    standButton.grid(column=2, row=4)
    standButton['command'] = lambda: stand(signInButton, doubleDownButton, hitButton, splitButton, standButton, doubleDownButton_2, hitButton_2, standButton_2)
    quitButton = Button(window, text='Quit', font='roman 12', fg='red', bg='grey')
    quitButton.grid(column=5, row=1)
    quitButton['command'] = lambda: close()
    player.money = player.money - 1
    player.potMoney = 1
    player.potMoney_2 = 0
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
        showNewHandButton(signInButton)
    
window = Tk()
player = Player()
dealer = Player()
player.isdealer = False
connectDB()
gameMsg = Label(window, text='', font='roman 35 bold', fg='white', bg='#01550a')
gameMsg.grid(column=10, row=4)
gameMsg_2 = Label(window, text='BlackJack', font='roman 40 bold', fg='white', bg='#01550a')
gameMsg_2.grid(column=2, row=9, columnspan=2)
setWindow(window, player)
deck = os.listdir('./deck_p')
window.mainloop()

