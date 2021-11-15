from tkinter import *
import tkinter as tk
import csv
from PIL import ImageTk, Image
import requests
import json
import urllib.request

root = Tk()
root.title("Crazy 8")
c = Canvas(root)
root.geometry('1500x900')
root.configure(bg='green')
player1ButtonList = [None, None, None, None, None, None, None]
player1CardImageList = [None, None, None, None, None, None, None]
player2ButtonList = [None, None, None, None, None, None, None]
player2CardImageList = [None, None, None, None, None, None, None]
global deck_id 

r = requests.get('https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1')
temp = r.json()
deck_id = temp['deck_id']
codeArr = []
# Initialize Both Hands
for x in range (1,3):
    for x in range (1,8):
#       Add card to player hand
        r = requests.get('https://deckofcardsapi.com/api/deck/'+deck_id+'/draw/?count=1')
        drawed_card = r.json()['cards']
        temp_drawed_card = drawed_card
        code = temp_drawed_card[0]['code']
        r = requests.get('https://deckofcardsapi.com/api/deck/'+deck_id+'/pile/player'+str(x)+'/add/?cards='+code)
        codeArr.append(code)
for x in codeArr :
        splitArr = list(str(x))
        print(splitArr)
        
        #display any aces
        if(len(splitArr) == 2 and splitArr[0] == 'A' and codeArr.index(x) < 7):
                player1CardImageList[codeArr.index(x)] = Image.open(splitArr[1].lower() + "01.png", mode='r')
                player1CardImageList[codeArr.index(x)] = player1CardImageList[codeArr.index(x)].resize((100,200), Image.ANTIALIAS)
                player1CardImageList[codeArr.index(x)] = ImageTk.PhotoImage(player1CardImageList[codeArr.index(x)])
                player1ButtonList[codeArr.index(x)] = Button(root, image=player1CardImageList[codeArr.index(x)], command=lambda: cardClicked(player1ButtonList[codeArr.index(x)]))
        elif(len(splitArr) == 2 and splitArr[0] == 'A' and codeArr.index(x) >= 7):
                player2CardImageList[codeArr.index(x)-7] = Image.open(splitArr[1].lower() + "01.png", mode='r')
                player2CardImageList[codeArr.index(x)-7] = player2CardImageList[codeArr.index(x)-7].resize((100,200), Image.ANTIALIAS)
                player2CardImageList[codeArr.index(x)-7] = ImageTk.PhotoImage(player2CardImageList[codeArr.index(x)-7])
                player2ButtonList[codeArr.index(x)-7] = Button(root, image=player2CardImageList[codeArr.index(x)-7], command=lambda: cardClicked(player2ButtonList[codeArr.index(x)-7]))
        
        #display any kings
        elif (len(splitArr) == 2 and splitArr[0] == 'K' and codeArr.index(x) < 7):
                player1CardImageList[codeArr.index(x)] = Image.open(splitArr[1].lower() + "13.png", mode='r')
                player1CardImageList[codeArr.index(x)] = player1CardImageList[codeArr.index(x)].resize((100,200), Image.ANTIALIAS)
                player1CardImageList[codeArr.index(x)] = ImageTk.PhotoImage(player1CardImageList[codeArr.index(x)])
                player1ButtonList[codeArr.index(x)] = Button(root, image=player1CardImageList[codeArr.index(x)], command=lambda: cardClicked(player1ButtonList[codeArr.index(x)]))
        elif (len(splitArr) == 2 and splitArr[0] == 'K' and codeArr.index(x) >= 7):
                player2CardImageList[codeArr.index(x)-7] = Image.open(splitArr[1].lower() + "13.png", mode='r')
                player2CardImageList[codeArr.index(x)-7] = player2CardImageList[codeArr.index(x)-7].resize((100,200), Image.ANTIALIAS)
                player2CardImageList[codeArr.index(x)-7] = ImageTk.PhotoImage(player2CardImageList[codeArr.index(x)-7])
                player2ButtonList[codeArr.index(x)-7] = Button(root, image=player2CardImageList[codeArr.index(x)-7], command=lambda: cardClicked(player2ButtonList[codeArr.index(x)-7]))

        #display any queens
        elif (len(splitArr) == 2 and splitArr[0] == 'Q' and codeArr.index(x) < 7):
                player1CardImageList[codeArr.index(x)] = Image.open(splitArr[1].lower() + "12.png", mode='r')
                player1CardImageList[codeArr.index(x)] = player1CardImageList[codeArr.index(x)].resize((100,200), Image.ANTIALIAS)
                player1CardImageList[codeArr.index(x)] = ImageTk.PhotoImage(player1CardImageList[codeArr.index(x)])
                player1ButtonList[codeArr.index(x)] = Button(root, image=player1CardImageList[codeArr.index(x)], command=lambda: cardClicked(player1ButtonList[codeArr.index(x)]))
        elif (len(splitArr) == 2 and splitArr[0] == 'Q' and codeArr.index(x) >= 7):
                player2CardImageList[codeArr.index(x)-7] = Image.open(splitArr[1].lower() + "12.png", mode='r')
                player2CardImageList[codeArr.index(x)-7] = player2CardImageList[codeArr.index(x)-7].resize((100,200), Image.ANTIALIAS)
                player2CardImageList[codeArr.index(x)-7] = ImageTk.PhotoImage(player2CardImageList[codeArr.index(x)-7])
                player2ButtonList[codeArr.index(x)-7] = Button(root, image=player2CardImageList[codeArr.index(x)-7], command=lambda: cardClicked(player2ButtonList[codeArr.index(x)-7]))
        
        #display any 10s
        elif (len(splitArr) == 2 and splitArr[0] == '0' and codeArr.index(x) < 7):
                player1CardImageList[codeArr.index(x)-7] = Image.open(splitArr[1].lower() + "10.png", mode='r')
                player1CardImageList[codeArr.index(x)] = player1CardImageList[codeArr.index(x)].resize((100,200), Image.ANTIALIAS)
                player1CardImageList[codeArr.index(x)-7] = ImageTk.PhotoImage(player1CardImageList[codeArr.index(x)-7])
                player1ButtonList[codeArr.index(x)-7] = Button(root, image=player1CardImageList[codeArr.index(x)-7], command=lambda: cardClicked(player1ButtonList[codeArr.index(x)-7]))
        elif (len(splitArr) == 2 and splitArr[0] == '0' and codeArr.index(x) >= 7):
                player2CardImageList[codeArr.index(x)-7] = Image.open(splitArr[1].lower() + "10.png", mode='r')
                player2CardImageList[codeArr.index(x)-7] = player2CardImageList[codeArr.index(x)-7].resize((100,200), Image.ANTIALIAS)
                player2CardImageList[codeArr.index(x)-7] = ImageTk.PhotoImage(player2CardImageList[codeArr.index(x)-7])
                player2ButtonList[codeArr.index(x)-7] = Button(root, image=player2CardImageList[codeArr.index(x)-7], command=lambda: cardClicked(player2ButtonList[codeArr.index(x)-7]))     
        
        #display any jacks        
        elif (len(splitArr) == 2 and splitArr[0] == 'J' and codeArr.index(x) < 7):
                player1CardImageList[codeArr.index(x)-7] = Image.open(splitArr[1].lower() + "11.png", mode='r')
                player1CardImageList[codeArr.index(x)] = player1CardImageList[codeArr.index(x)].resize((100,200), Image.ANTIALIAS)
                player1CardImageList[codeArr.index(x)-7] = ImageTk.PhotoImage(player1CardImageList[codeArr.index(x)-7])
                player1ButtonList[codeArr.index(x)-7] = Button(root, image=player1CardImageList[codeArr.index(x)-7], command=lambda: cardClicked(player1ButtonList[codeArr.index(x)-7]))
        elif (len(splitArr) == 2 and splitArr[0] == 'J' and codeArr.index(x) >= 7):
                player2CardImageList[codeArr.index(x)-7] = Image.open(splitArr[1].lower() + "11.png", mode='r')
                player2CardImageList[codeArr.index(x)-7] = player2CardImageList[codeArr.index(x)-7].resize((100,200), Image.ANTIALIAS)
                player2CardImageList[codeArr.index(x)-7] = ImageTk.PhotoImage(player2CardImageList[codeArr.index(x)-7])
                player2ButtonList[codeArr.index(x)-7] = Button(root, image=player2CardImageList[codeArr.index(x)-7], command=lambda: cardClicked(player2ButtonList[codeArr.index(x)-7])) 
        
                
        elif(len(splitArr) == 2 and codeArr.index(x) < 7):
                player1CardImageList[codeArr.index(x)-7] = Image.open(str(splitArr[1]).lower() + '0' + str(splitArr[0]) + ".png", mode='r')
                player1CardImageList[codeArr.index(x)] = player1CardImageList[codeArr.index(x)].resize((100,200), Image.ANTIALIAS)
                player1CardImageList[codeArr.index(x)-7] = ImageTk.PhotoImage(player1CardImageList[codeArr.index(x)-7])
                player1ButtonList[codeArr.index(x)-7] = Button(root, image=player1CardImageList[codeArr.index(x)-7], command=lambda: cardClicked(player1ButtonList[codeArr.index(x)-7]))
        elif(len(splitArr) == 2 and codeArr.index(x) >= 7):
                player2CardImageList[codeArr.index(x)-7] = Image.open(str(splitArr[1]).lower() + '0' + str(splitArr[0]) + ".png", mode='r')
                player2CardImageList[codeArr.index(x)-7] = player2CardImageList[codeArr.index(x)-7].resize((100,200), Image.ANTIALIAS)
                player2CardImageList[codeArr.index(x)-7] = ImageTk.PhotoImage(player2CardImageList[codeArr.index(x)-7])
                player2ButtonList[codeArr.index(x)-7] = Button(root, image=player2CardImageList[codeArr.index(x)-7], command=lambda: cardClicked(player2ButtonList[codeArr.index(x)-7]))
        
        
        elif(len(splitArr) == 3 and codeArr.index(x) < 7):
                player1CardImageList[codeArr.index(x)-7] = Image.open(str(splitArr[3]).lower() + str(splitArr[0])  + str(splitArr[1]) + ".png", mode='r')
                player1CardImageList[codeArr.index(x)] = player1CardImageList[codeArr.index(x)].resize((100,200), Image.ANTIALIAS)
                player1CardImageList[codeArr.index(x)-7] = ImageTk.PhotoImage(player1CardImageList[codeArr.index(x)-7])
                player1ButtonList[codeArr.index(x)-7] = Button(root, image=player1CardImageList[codeArr.index(x)-7], command=lambda: cardClicked(player1ButtonList[codeArr.index(x)-7]))
        elif(len(splitArr) == 3 and codeArr.index(x) >= 7):
                player2CardImageList[codeArr.index(x)-7] = Image.open(str(splitArr[3]).lower() + str(splitArr[0])  + str(splitArr[1]) + ".png", mode='r')
                player2CardImageList[codeArr.index(x)-7] = player2CardImageList[codeArr.index(x)-7].resize((100,200), Image.ANTIALIAS)
                player2CardImageList[codeArr.index(x)-7] = ImageTk.PhotoImage(player2CardImageList[codeArr.index(x)-7])
                player2ButtonList[codeArr.index(x)-7] = Button(root, image=player2CardImageList[codeArr.index(x)-7], command=lambda: cardClicked(player2ButtonList[codeArr.index(x)-7]))
        
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

x1 = 30
y1 = 450
x2 = 30
y2 = 670
for x in player1ButtonList:
    x1 += 150
    x.place(x=x1,y=y1)
for y in player2ButtonList:
    x2 += 150
    y.place(x=x2,y=y2)
        
def start_game():
    pass
def draw_card():
    r = requests.get('https://deckofcardsapi.com/api/deck/'+deck_id+'/draw/?count=1')
    drawed_card = r.json()['cards']
    code = drawed_card[0]['code']
    return drawed_card
      
def cardClicked(b):
    pass

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
