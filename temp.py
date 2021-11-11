import requests, json
import urllib.request
from PIL import Image

deck_id = 0

def start_game():
    """Makes a new deck, discard\n
    Adds 7 cards to each player
    """
    global deck_id
    r = requests.get('https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1')
    print(r.json())
    temp = r.json()
    deck_id = temp['deck_id']
    # print(deck_id)
    # Initialize Discard
    temp_top_card = draw_card()
    r = requests.get('https://deckofcardsapi.com/api/deck/'+deck_id+'/pile/discard/add/?cards='+temp_top_card)
    # Initialize Both Hands
    for x in range (1,3):
        print('Giving Player '+str(x)+' cards')
        for y in range (1,8):
        #   Add card to player hand
            temp_drawed_card = draw_card()
            r = requests.get('https://deckofcardsapi.com/api/deck/'+deck_id+'/pile/player'+str(x)+'/add/?cards='+temp_drawed_card)

def check_player1_hand():
    """Checks the player hand\n
    Returns the hand codes in an array
    """
    temp_array = []
    r = requests.get('https://deckofcardsapi.com/api/deck/'+deck_id+'/pile/player1/list/')
    for temp in r.json()['piles']['player1']['cards']:
        temp_array.append(temp['code'])
    # print(temp_array)
    return(temp_array)

def check_player2_hand():
    """Checks the player hand\n
    Returns the hand codes in an array
    """
    temp_array = []
    r = requests.get('https://deckofcardsapi.com/api/deck/'+deck_id+'/pile/player2/list/')
    for temp in r.json()['piles']['player2']['cards']:
        temp_array.append(temp['code'])
    # print(temp_array)
    return(temp_array)

def draw_card():
    """Draws a card from the deck\n 
    Returns the card code 
    """
    # print('https://deckofcardsapi.com/api/deck/'+deck_id+'/draw/?count=1')
    r = requests.get('https://deckofcardsapi.com/api/deck/'+deck_id+'/draw/?count=1')
    # print(r.json())
    drawed_card = r.json()['cards']
    # print('Drawed Card: ' + str(drawed_card))
    print('Drawed Card: ' + str(drawed_card[0]['code']))
    # code = drawed_card[0]['code']
    return drawed_card[0]['code']

def draw_card_from_player1():
    r = requests.get('https://deckofcardsapi.com/api/deck/'+deck_id+'/pile/player1/draw/?count=1')
    drawed_card = r.json()['cards']
    return drawed_card[0]['code']

def draw_card_from_player2():
    r = requests.get('https://deckofcardsapi.com/api/deck/'+deck_id+'/pile/player2/draw/?count=1')
    drawed_card = r.json()['cards']
    return drawed_card[0]['code']

def add_to_discard(card):
    card_code = card[0]['code']
    r = requests.get('https://deckofcardsapi.com/api/deck/'+deck_id+'/pile/discard/add/?cards='+card_code)
    print(r.json())

def list_played_cards():
    r = requests.get('https://deckofcardsapi.com/api/deck/'+deck_id+'/pile/discard/list/')
    print(r.json())

def restart_game():
    r = requests.get('https://deckofcardsapi.com/api/deck/'+deck_id+'/pile/discard/return/')
    print('Restarted' + r.json())
    
# def get_card_image_debug():
#     r = requests.get('https://deckofcardsapi.com/api/deck/'+deck_id+'/pile/player2/draw/?count=7')
#     drawed_card = r.json()['cards']
#     for x in drawed_card:
#         print(x)

def playable(card):
    """Takes in a card CODE, not the entire json\n
    Compares this with the top of the discard for the faction and face value\n 
    Special Cases:\n
    Jack = 11\n
    Queen = 12\n
    King = 13\n
    Ace = 01\n
    10 = 0\n
    """
    r = requests.get('https://deckofcardsapi.com/api/deck/'+deck_id+'/pile/discard/list/')
    temp_card = r.json()['piles']['discard']['cards'][0]
    temp_code = temp_card['code']
    print(temp_code)
    if(temp_code[1]==card[1]):
        return True
    if(temp_code[0: 1]==card[0: 1]):
        return True
    return False

start_game()
print(check_player1_hand())
tempcard = draw_card_from_player1()
print(playable(tempcard))

# rtemp = requests.get('https://deckofcardsapi.com/api/deck/'+deck_id+'/pile/player1/draw/?count=1')
# print(rtemp.json())
# print(playable())