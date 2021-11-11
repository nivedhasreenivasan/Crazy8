import requests, json
import urllib.request
from PIL import Image


def start_game():
    global deck_id
    r = requests.get('https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1')
    print(r.json())
    temp = r.json()
    deck_id = temp['deck_id']
    print(deck_id)
    # Initialize Both Hands
    for x in range (1,3):
        print('Giving Player '+str(x)+' cards')
        for y in range (1,8):
    #       Add card to player hand
            temp_drawed_card = draw_card()
            code = temp_drawed_card[0]['code']
            r = requests.get('https://deckofcardsapi.com/api/deck/'+deck_id+'/pile/player'+str(x)+'/add/?cards='+code)

def check_player1_hand():
    r = requests.get('https://deckofcardsapi.com/api/deck/'+deck_id+'/pile/player1/list/')
    print(r.json())

def draw_card():
    # print('https://deckofcardsapi.com/api/deck/'+deck_id+'/draw/?count=1')
    r = requests.get('https://deckofcardsapi.com/api/deck/'+deck_id+'/draw/?count=1')
    # print(r.json())
    drawed_card = r.json()['cards']
    # print('Drawed Card: ' + str(drawed_card))
    print('Drawed Card: ' + str(drawed_card[0]['code']))
    # code = drawed_card[0]['code']
    return drawed_card 
    
def add_to_discard(card):
    card_code = card[0]['code']
    r = requests.get('https://deckofcardsapi.com/api/deck/'+deck_id+'/pile/discard/add/?cards='+card_code)
    print(r.json())

def list_played_cards():
    r = requests.get('https://deckofcardsapi.com/api/deck/'+deck_id+'/pile/discard/list/')
    print(r.json())

def restart_game():
    r = requests.get('https://deckofcardsapi.com/api/deck/'+deck_id+'/pile/discard/return/')
    print(r.json())
    
def playable(card):
    card_code = card[0]['code']
    r = requests.get('https://deckofcardsapi.com/api/deck/'+deck_id+'/pile/discard/return/')
    temp_card = r.json()['piles']['discard']['cards'][0]
    print(temp_card)
    temp_code = temp_card[0]['code']
    if(temp_code[1]==card_code[1]):
        return True
    if(temp_code[0: 1]==card_code[0: 1]):
        return True

start_game()
# check_player1_hand()