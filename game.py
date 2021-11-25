from tkinter import *
import tkinter as tk
import csv
from PIL import ImageTk, Image
import requests
import json
from io import BytesIO
from urllib.request import Request, urlopen

root = Tk()
root.title("Crazy 8")
c = Canvas(root)
root.geometry('1500x900')
root.configure(bg='green')
player1ButtonList = []
player2ButtonList = []
global deck_id 
global player1Turn
global player2Turn
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

#Create menu
my_menu = Menu(root)
root.config(menu=my_menu)
#Create Options Menu
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='Options', menu= options_menu)
options_menu.add_command(label="Reset")
playerNum = 1 #default
w = tk.Label(root, text="Player " + str(playerNum))
# w.place(relx = 25.0,rely = 450.0, anchor = 'center')       
w.pack()
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
          
player1Turn = True
player2Turn = False

def add_to_discard(cardcode):
    r = requests.get('https://deckofcardsapi.com/api/deck/'+deck_id+'/pile/discard/add/?cards='+cardcode)
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

def drawAndPlaceCardForPlayer(str):
    drawnCard = draw_card()
    requests.get('https://deckofcardsapi.com/api/deck/'+deck_id+'/pile/discard/add/?cards='+drawnCard)
    imageStart = 'https://deckofcardsapi.com/static/img/'  + drawnCard + '.png'
    u = Request(imageStart, headers={'User-Agent': 'Mozilla/5.0'})
    raw_data = urlopen(u).read()
    im = Image.open(BytesIO(raw_data))
    im = im.resize((100,200),Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(im)
    addedCard= tk.Button(image=photo,width=100,height=200,compound="c")
    addedCard.image = photo
    list = [addedCard,drawnCard]
    if (str == 'player1'):
        player1ButtonList.append(list)
        x1 = 30
        y1 = 450
        for x in player1ButtonList:
            x1 += 150
            x[0].place(x=x1,y=y1)
    elif (str == 'player2'):
        player2ButtonList.append(list)
        x2 = 30
        y2 = 670
        for x in player2ButtonList:
            x2 += 150
            x[0].place(x=x2,y=y2)
    # if (player1Turn == True):
    #     player1Turn == False
    #     player2Turn == True
    # elif(player2Turn == True):
    #     player2Turn == False
    #     player1Turn == True
    
    #add_to_discard(code)

#place the first discard card
temp_top_card = draw_card()
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
drawButton1 = Button(root, text="DRAW CARD", font=("Helvetica", 10), height = 3, width = 10, bg="SystemButtonFace", command=lambda: drawAndPlaceCardForPlayer("player1"))
drawButton1.place(x = 30, y = 450)

drawButton2 = Button(root, text="DRAW CARD", font=("Helvetica", 10), height = 3, width = 10, bg="SystemButtonFace", command=lambda: drawAndPlaceCardForPlayer("player2"))
drawButton2.place(x = 30, y = 670)

def cardClicked(b, playername):
    print(playername == 'player1')
    global temp_top_card
    if( player1Turn == True and playername == 'player1' and b[0:1] == temp_top_card[0:1]):
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
                player1Turn == False
                player2Turn == True
        # for x in player2ButtonList:
        #     if(x[1] == b):
        #         x[0].destroy() 
        #         player2ButtonList.remove(x)
    # elif(len(temp_top_card) == 3 and len(b) == 3 and (b[1:3] == temp_top_card[1:3])):
    #     temp_top_card = b
    #     requests.get('https://deckofcardsapi.com/api/deck/'+deck_id+'/pile/discard/add/?cards='+temp_top_card)
    #     imageStart = 'https://deckofcardsapi.com/static/img/'  + temp_top_card + '.png'
    #     u = Request(imageStart, headers={'User-Agent': 'Mozilla/5.0'})
    #     raw_data = urlopen(u).read()
    #     im = Image.open(BytesIO(raw_data))
    #     im = im.resize((100,200),Image.ANTIALIAS)
    #     photo = ImageTk.PhotoImage(im)
    #     buttonDiscard = tk.Button(image=photo,width=100,height=200,compound="c")
    #     buttonDiscard.image = photo
    #     buttonDiscard.place(x = 700, y = 80)
        
    #     for x in player1ButtonList:
    #         if(x[1] == b):
    #             x[0].destroy()
    #             player1ButtonList.remove(x)
    #     for x in player2ButtonList:
    #         if(x[1] == b):
    #             x[0].destroy()
    #             player2ButtonList.remove(x) 
    # elif(len(temp_top_card) == 2 and len(b) == 2 and (b[1:2] == temp_top_card[1:2])):
    #     temp_top_card = b
    #     requests.get('https://deckofcardsapi.com/api/deck/'+deck_id+'/pile/discard/add/?cards='+temp_top_card)
    #     imageStart = 'https://deckofcardsapi.com/static/img/'  + temp_top_card + '.png'
    #     u = Request(imageStart, headers={'User-Agent': 'Mozilla/5.0'})
    #     raw_data = urlopen(u).read()
    #     im = Image.open(BytesIO(raw_data))
    #     im = im.resize((100,200),Image.ANTIALIAS)
    #     photo = ImageTk.PhotoImage(im)
    #     buttonDiscard = tk.Button(image=photo,width=100,height=200,compound="c")
    #     buttonDiscard.image = photo
    #     buttonDiscard.place(x = 700, y = 80)
        
    #     for x in player1ButtonList:
    #         if(x[1] == b):
    #             x[0].destroy()
    #             player1ButtonList.remove(x)
    #     for x in player2ButtonList:
    #         if(x[1] == b):
    #             x[0].destroy() 
    #             player2ButtonList.remove(x)
                
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
    

def restart_game():
    r = requests.get('https://deckofcardsapi.com/api/deck/'+deck_id+'/pile/discard/return/')
    print(r.json())

def skip(self):
    global skipButton
    global clicked
    self.clicked = True
    skipButton = Button(root, text="SKIP", font=("Helvetica", 7), height = 3, width = 9, bg="SystemButtonFace", command=lambda: skip_click(skipButton))
    skipButton.place(x=710,y=650)


root.mainloop()
