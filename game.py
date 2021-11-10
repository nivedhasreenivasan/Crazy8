from tkinter import *
import tkinter as tk
import csv
from PIL import ImageTk, Image
import requests
import json

root = Tk()
root.title("Crazy 8")
c = Canvas(root)
root.geometry('1500x900')
c.pack(fill=BOTH, expand=True)
#Create menu
my_menu = Menu(root)
root.config(menu=my_menu)
#Create Options Menu
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='Options', menu= options_menu)
options_menu.add_command(label="Reset")
player1Count = 0
player2Count = 0
playerNum = 1 #default
w = tk.Label(root, text="Player " + str(playerNum))
w.pack()

def start_game():
    global deck_id
    r = requests.get('https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1')
    print(r.json())
    temp = r.json()
    deck_id = temp['deck_id']
    global imageArr
    #print(deck_id)
    # Initialize Both Hands
    for x in range (1,3):
        for x in range (1,8):
    #       Add card to player hand
            temp_drawed_card = draw_card()
            code = temp_drawed_card[0]['code']
            image = temp_drawed_card[0]['image']
            r = requests.get('https://deckofcardsapi.com/api/deck/'+deck_id+'/pile/player'+str(x)+'/add/?cards='+code)
            imageArr = imageArr.append(image)
    for x in imageArr:
        cardImage = Image.open(str(x), mode='r')
        cardImage = ImageTk.PhotoImage(cardImage)
        u = Button(root, image=cardImage, command=lambda: cardClicked(u))
        u.place(x=600,y=525)

def cardClicked():

def draw_card():
    # print('https://deckofcardsapi.com/api/deck/'+deck_id+'/draw/?count=1')
    r = requests.get('https://deckofcardsapi.com/api/deck/'+deck_id+'/draw/?count=1')
    # print(r.json())
    drawed_card = r.json()['cards']
    # code = drawed_card[0]['code']
    return drawed_card

def add_to_discard(card):
    card_code = card['code']
    r = requests.get('https://deckofcardsapi.com/api/deck/'+deck_id+'/pile/discard/add/?cards='+card_code)
    print(r.json())

def list_played_cards():
    r = requests.get('https://deckofcardsapi.com/api/deck/'+deck_id+'/pile/discard/list/')
    print(r.json())

def restart_game():
    r = requests.get('https://deckofcardsapi.com/api/deck/'+deck_id+'/pile/discard/return/')
    print(r.json())

start_game()
def skip(self):
    global skipButton
    global clicked
    self.clicked = True
    skipButton = Button(root, text="SKIP", font=("Helvetica", 7), height = 3, width = 9, bg="SystemButtonFace", command=lambda: skip_click(skipButton))
    skipButton.place(x=710,y=650)

def turn(self): #does not work
    global player1Turn
    global player2Turn
    if (player1Count == player2Count):
        player1Turn = True
    elif (player1Count > player2Count):
        player2Turn = True
    elif (player1Count < player2Count):
        player1Turn = True
    if (self.clicked == True and player1Turn == True):
        player1Turn == False
    elif (self.clicked == True and player2Turn == True):
        player2Turn == False
root.mainloop()
