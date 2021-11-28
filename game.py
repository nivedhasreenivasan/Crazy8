from tkinter import *
import tkinter as tk
import csv
from PIL import ImageTk, Image
import requests
import json
from io import BytesIO
from urllib.request import HTTPDefaultErrorHandler, Request, urlopen
from tkinter import messagebox
from requests.models import to_native_string

root = Tk()
root.title("Crazy 8")
c = Canvas(root)
root.geometry('1500x900')
root.configure(bg='green')
player1ButtonList = []
player2ButtonList = []
global deck_id 
temp_top_card = None
currentClickedCard = None
player1Turn = False
player2Turn = True
listOfCards = {"AH", "AC", "AS", "AD", "2H", "2C", "2S", "2D", "3H", "3C", "3S", "3D", "4H", "4C", "4S", "4D", "5H", "5C", "5S", "5D", "6H", "6C", "6S", "6D", "7H", "7C", "7S", "7D", "8H", "8C", "8S", "8D", "9H", "9C", "9S", "9D", "0H", "0C", "0S", "0D", "JH", "JC", "JS", "JD", "QH", "QC", "QS", "QD", "KH", "KC", "KS", "KD"}

r = requests.get('https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1')
temp = r.json()
deck_id = temp['deck_id']
codeArr = []
imageArr = []
# Initialize Both Hands
for x in range (1,3):
    for y in range (1,8):
#       Add card to player hand
        r = requests.get('https://deckofcardsapi.com/api/deck/'+deck_id+'/draw/?count=1')
        drawed_card = r.json()['cards']
        temp_drawed_card = drawed_card
        code = temp_drawed_card[0]['code']
        r = requests.get('https://deckofcardsapi.com/api/deck/'+deck_id+'/pile/player'+str(x)+'/add/?cards='+code)
        image = temp_drawed_card[0]['image']
        imageArr.append(image)
        # print(imageArr)
        codeArr.append(code)
        r = requests.get('https://deckofcardsapi.com/api/deck/'+deck_id+'/pile/discard/add/?cards='+code)
for x in imageArr:
    u = Request(x, headers={'User-Agent': 'Mozilla/5.0'})
    raw_data = urlopen(u).read()

    im = Image.open(BytesIO(raw_data))
    im = im.resize((100,200),Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(im)

    if(imageArr.index(x) < 7):
        button = tk.Button(image=photo,width=100,height=200,compound="c", command=lambda code=codeArr[imageArr.index(x)]: cardClicked(code, 'player1'))
        print(button)
        button.image = photo
        list = [button,codeArr[imageArr.index(x)]]
        player1ButtonList.append(list)
    else:
        button = tk.Button(image=photo,width=100,height=200,compound="c", command=lambda code=codeArr[imageArr.index(x)]: cardClicked(code, 'player2'))
        button.image = photo
        list = [button,codeArr[imageArr.index(x)]]
        player2ButtonList.append(list)
print(player1ButtonList)        
print(player2ButtonList)
crazy8Choice = None
x1 = 30
y1 = 450
x2 = 30
y2 = 670
for x in player1ButtonList:
    x1 += 150
    x[0].place(x=x1,y=y1)
for y in player2ButtonList:
    x2 += 150
    y[0].place(x=x2,y=y2)
    
def crazy8Pick(crazy8Choice):
    global currentClickedCard
    global temp_top_card
    temp_top_card = crazy8Choice
    requests.get('https://deckofcardsapi.com/api/deck/'+deck_id+'/pile/discard/add/?cards='+temp_top_card)
    imageStart = 'https://deckofcardsapi.com/static/img/'  + temp_top_card + '.png'
    u = Request(imageStart, headers={'User-Agent': 'Mozilla/5.0'})
    raw_data = urlopen(u).read()
    im = Image.open(BytesIO(raw_data))
    im = im.resize((100,200),Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(im)
    buttonDiscard = tk.Button(image=photo,width=100,height=200,compound="c")
    buttonDiscard.image = photo
    buttonDiscard.place(x = 700, y = 80)
    
    for z in player1ButtonList:
        print(player1ButtonList)
        if(z[1] == currentClickedCard):
            z[0].destroy()
            print(player1ButtonList)
            player1ButtonList.remove(z)
            cardMenu.configure(state="disabled")
            x1 = 30
            y1 = 450
            x2 = 30
            y2 = 670
            for x in player1ButtonList:
                x1 += 150
                x[0].place(x=x1,y=y1)
            for y in player2ButtonList:
                x2 += 150
                y[0].place(x=x2,y=y2)   
            changePlayer()
    for a in player2ButtonList:
        print(player2ButtonList)
        if(a[1] == currentClickedCard):
            a[0].destroy()
            print(player2ButtonList)
            player2ButtonList.remove(a)
            cardMenu.configure(state="disabled")
            x1 = 30
            y1 = 450
            x2 = 30
            y2 = 670
            for x in player1ButtonList:
                x1 += 150
                x[0].place(x=x1,y=y1)
            for y in player2ButtonList:
                x2 += 150
                y[0].place(x=x2,y=y2)   
            changePlayer()
        # winner
    if (len(player2ButtonList) == 0):
        messagebox.showinfo('WINNER', 'PLAYER 2 WINS!')
    elif (len(player1ButtonList) == 0):
        messagebox.showinfo('WINNER', 'PLAYER 1 WINS!')
x1 = 30
y1 = 450
x2 = 30
y2 = 670
for x in player1ButtonList:
    x1 += 150
    x[0].place(x=x1,y=y1)
for y in player2ButtonList:
    x2 += 150
    y[0].place(x=x2,y=y2)       
    
def display_selected (choice):
    global crazy8Choice
    choice = variable.get()
    crazy8Choice = choice
    crazy8Pick(crazy8Choice)
    
variable = StringVar(root)
variable.set("pick a card (if 8 was placed)") # default value
cardMenu = OptionMenu(root, variable, *listOfCards, command = display_selected)
cardMenu.place(x = 700, y = 20)
cardMenu.configure(state="disabled")

def add_to_discard(cardcode):
    r = requests.get('https://deckofcardsapi.com/api/deck/' + deck_id + '/return/?cards='+cardcode)
    print(r.json())
    
def draw_card():
    r = requests.get('https://deckofcardsapi.com/api/deck/'+deck_id+'/draw/?count=1')
    drawed_card = r.json()['cards']
    code = drawed_card[0]['code']
    r = requests.get('https://deckofcardsapi.com/api/deck/'+deck_id+'/pile/player'+str(x)+'/add/?cards='+code)
    image = temp_drawed_card[0]['image']
    imageArr.append(image)
    # print(imageArr)
    codeArr.append(code)
    add_to_discard(code)
    return code

def drawAndPlaceCardForPlayer1():
    if(player1Turn == True):
        drawnCard = draw_card()
        requests.get('https://deckofcardsapi.com/api/deck/'+deck_id+'/pile/discard/add/?cards='+drawnCard)
        imageStart = 'https://deckofcardsapi.com/static/img/'  + drawnCard + '.png'
        u = Request(imageStart, headers={'User-Agent': 'Mozilla/5.0'})
        raw_data = urlopen(u).read()
        im = Image.open(BytesIO(raw_data))
        im = im.resize((100,200),Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(im)
        addedCard= tk.Button(image=photo,width=100,height=200,compound="c",command=lambda code=drawnCard: cardClicked(code,'player1'))
        addedCard.image = photo
        list = [addedCard,drawnCard]
        player1ButtonList.append(list)
        x1 = 30
        y1 = 450
        for x in player1ButtonList:
            x1 += 150
            x[0].place(x=x1,y=y1)
        changePlayer()                
            
def drawAndPlaceCardForPlayer2():
    if(player2Turn == True):
        drawnCard = draw_card()
        requests.get('https://deckofcardsapi.com/api/deck/'+deck_id+'/pile/discard/add/?cards='+drawnCard)
        imageStart = 'https://deckofcardsapi.com/static/img/'  + drawnCard + '.png'
        u = Request(imageStart, headers={'User-Agent': 'Mozilla/5.0'})
        raw_data = urlopen(u).read()
        im = Image.open(BytesIO(raw_data))
        im = im.resize((100,200),Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(im)
        addedCard= tk.Button(image=photo,width=100,height=200,compound="c",command=lambda code=drawnCard: cardClicked(code,'player2'))
        addedCard.image = photo
        list = [addedCard,drawnCard]
        player2ButtonList.append(list)
        x2 = 30
        y2 = 670
        for x in player2ButtonList:
            x2 += 150
            x[0].place(x=x2,y=y2)
        changePlayer()


def changePlayer():
    global player1Turn, player2Turn
    if(player1Turn == True):
       player1Turn = False
       player2Turn = True
    elif(player2Turn == True):
       player2Turn = False
       player1Turn = True
       
#place the first discard card
temp_top_card = draw_card()
if(temp_top_card[0:1] == '8'):
    changePlayer() 
    cardMenu.configure(state="normal")
    
requests.get('https://deckofcardsapi.com/api/deck/'+deck_id+'/pile/discard/add/?cards='+temp_top_card)
imageStart = 'https://deckofcardsapi.com/static/img/'  + temp_top_card + '.png'
u = Request(imageStart, headers={'User-Agent': 'Mozilla/5.0'})
raw_data = urlopen(u).read()
im = Image.open(BytesIO(raw_data))
im = im.resize((100,200),Image.ANTIALIAS)
photo = ImageTk.PhotoImage(im)
buttonDiscard = tk.Button(image=photo,width=100,height=200,compound="c")
buttonDiscard.image = photo
buttonDiscard.place(x = 700, y = 80)        
# print(check_player1_hand())
# print(check_player2_hand())

#create draw button
drawButton1 = Button(root, text="DRAW CARD\nPLAYER 1 --->", font=("Helvetica", 10), height = 3, width = 10, bg="SystemButtonFace", command=lambda: drawAndPlaceCardForPlayer1())
drawButton1.place(x = 30, y = 450)

drawButton2 = Button(root, text="DRAW CARD\nPLAYER 2 --->", font=("Helvetica", 10), height = 3, width = 10, bg="SystemButtonFace", command=lambda: drawAndPlaceCardForPlayer2())
drawButton2.place(x = 30, y = 670)
    
# print(player1ButtonList)
# print(player2ButtonList)
def cardClicked(b, playername):
    global cardMenu
    global temp_top_card
    global currentClickedCard
    currentClickedCard = b
    if(player1Turn == True and playername == 'player1' and currentClickedCard[0:1] == '8'):
        cardMenu.configure(state="normal")
    elif(player2Turn == True and playername == 'player2' and currentClickedCard[0:1] == '8'):
        cardMenu.configure(state="normal")
    elif( player1Turn == True and playername == 'player1' and b[0:1] == temp_top_card[0:1]):
        temp_top_card = b
        requests.get('https://deckofcardsapi.com/api/deck/'+deck_id+'/pile/discard/add/?cards='+temp_top_card)
        imageStart = 'https://deckofcardsapi.com/static/img/'  + temp_top_card + '.png'
        u = Request(imageStart, headers={'User-Agent': 'Mozilla/5.0'})
        raw_data = urlopen(u).read()
        im = Image.open(BytesIO(raw_data))
        im = im.resize((100,200),Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(im)
        buttonDiscard = tk.Button(image=photo,width=100,height=200,compound="c")
        buttonDiscard.image = photo
        buttonDiscard.place(x = 700, y = 80)
        
        for x in player1ButtonList:
            if(x[1] == b):
                x[0].destroy()
                player1ButtonList.remove(x)
        changePlayer()            
    elif( player2Turn == True and playername == 'player2' and b[0:1] == temp_top_card[0:1]):
        temp_top_card = b
        requests.get('https://deckofcardsapi.com/api/deck/'+deck_id+'/pile/discard/add/?cards='+temp_top_card)
        imageStart = 'https://deckofcardsapi.com/static/img/'  + temp_top_card + '.png'
        u = Request(imageStart, headers={'User-Agent': 'Mozilla/5.0'})
        raw_data = urlopen(u).read()
        im = Image.open(BytesIO(raw_data))
        im = im.resize((100,200),Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(im)
        buttonDiscard = tk.Button(image=photo,width=100,height=200,compound="c")
        buttonDiscard.image = photo
        buttonDiscard.place(x = 700, y = 80)
    
        for x in player2ButtonList:
            if(x[1] == b):
                x[0].destroy() 
                player2ButtonList.remove(x)
        changePlayer()
        
    elif(player1Turn == True and playername == 'player1' and len(temp_top_card) == 3 and len(b) == 3 and (b[1:3] == temp_top_card[1:3])):
        temp_top_card = b
        requests.get('https://deckofcardsapi.com/api/deck/'+deck_id+'/pile/discard/add/?cards='+temp_top_card)
        imageStart = 'https://deckofcardsapi.com/static/img/'  + temp_top_card + '.png'
        u = Request(imageStart, headers={'User-Agent': 'Mozilla/5.0'})
        raw_data = urlopen(u).read()
        im = Image.open(BytesIO(raw_data))
        im = im.resize((100,200),Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(im)
        buttonDiscard = tk.Button(image=photo,width=100,height=200,compound="c")
        buttonDiscard.image = photo
        buttonDiscard.place(x = 700, y = 80)
        
        for x in player1ButtonList:
            if(x[1] == b):
                x[0].destroy()
                player1ButtonList.remove(x)
        changePlayer()      
          
    elif(player2Turn == True and playername == 'player2' and len(temp_top_card) == 3 and len(b) == 3 and (b[1:3] == temp_top_card[1:3])):
        temp_top_card = b
        requests.get('https://deckofcardsapi.com/api/deck/'+deck_id+'/pile/discard/add/?cards='+temp_top_card)
        imageStart = 'https://deckofcardsapi.com/static/img/'  + temp_top_card + '.png'
        u = Request(imageStart, headers={'User-Agent': 'Mozilla/5.0'})
        raw_data = urlopen(u).read()
        im = Image.open(BytesIO(raw_data))
        im = im.resize((100,200),Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(im)
        buttonDiscard = tk.Button(image=photo,width=100,height=200,compound="c")
        buttonDiscard.image = photo
        for x in player2ButtonList:
            if(x[1] == b):
                x[0].destroy()
                player2ButtonList.remove(x) 
        changePlayer()
        
    elif(player1Turn == True and playername == 'player1' and len(temp_top_card) == 2 and len(b) == 2 and (b[1:2] == temp_top_card[1:2])):
        temp_top_card = b
        requests.get('https://deckofcardsapi.com/api/deck/'+deck_id+'/pile/discard/add/?cards='+temp_top_card)
        imageStart = 'https://deckofcardsapi.com/static/img/'  + temp_top_card + '.png'
        u = Request(imageStart, headers={'User-Agent': 'Mozilla/5.0'})
        raw_data = urlopen(u).read()
        im = Image.open(BytesIO(raw_data))
        im = im.resize((100,200),Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(im)
        buttonDiscard = tk.Button(image=photo,width=100,height=200,compound="c")
        buttonDiscard.image = photo
        buttonDiscard.place(x = 700, y = 80)
        
        for x in player1ButtonList:
            if(x[1] == b):
                x[0].destroy()
                player1ButtonList.remove(x)
        changePlayer()
        
    elif(player2Turn == True and playername == 'player2' and len(temp_top_card) == 2 and len(b) == 2 and (b[1:2] == temp_top_card[1:2])):
        temp_top_card = b
        requests.get('https://deckofcardsapi.com/api/deck/'+deck_id+'/pile/discard/add/?cards='+temp_top_card)
        imageStart = 'https://deckofcardsapi.com/static/img/'  + temp_top_card + '.png'
        u = Request(imageStart, headers={'User-Agent': 'Mozilla/5.0'})
        raw_data = urlopen(u).read()
        im = Image.open(BytesIO(raw_data))
        im = im.resize((100,200),Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(im)
        buttonDiscard = tk.Button(image=photo,width=100,height=200,compound="c")
        buttonDiscard.image = photo
        buttonDiscard.place(x = 700, y = 80)
        for x in player2ButtonList:
            if(x[1] == b):
                x[0].destroy() 
                player2ButtonList.remove(x)
        changePlayer()        
    x1 = 30
    y1 = 450
    x2 = 30
    y2 = 670
    for x in player1ButtonList:
        x1 += 150
        x[0].place(x=x1,y=y1)
    for y in player2ButtonList:
        x2 += 150
        y[0].place(x=x2,y=y2)            
    # print(temp_top_card)
    # print(player1ButtonList)
    # print(player2ButtonList)
    
    # winner
    if (len(player2ButtonList) == 0):
        messagebox.showinfo('WINNER', 'PLAYER 2 WINS!')
    elif (len(player1ButtonList) == 0):
        messagebox.showinfo('WINNER', 'PLAYER 1 WINS!')
        
root.mainloop()
