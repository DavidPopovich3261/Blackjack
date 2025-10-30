
from core import player_io


def calculate_hand_value(hand: list[dict]) -> int:
    ranke={'a':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,"8":8,'9':9,'10':10,'j':10,"q":10,'k':10}
    c=0
    for i in hand:
        c+=ranke[i['rank']]
    return c






def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    player['hand'].append(deck.pop())
    player['hand'].append(deck.pop())
    dealer['hand'].append(deck.pop())
    dealer['hand'].append(deck.pop())
    value_player=calculate_hand_value(player['hand'])
    print('value_player',value_player)
    value_dealer=calculate_hand_value(dealer['hand'])
    print('value_dealer',value_dealer)





def dealer_play(deck: list[dict], dealer: dict) -> bool:
    while True:
        c=calculate_hand_value(dealer['hand'])
        if c < 17:
            dealer['hand'].append(deck.pop())
        c=calculate_hand_value(dealer['hand'])
        if c >=21:
            print('dealer loos')
            return False
        if c>=17:
            return True




def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    deal_two_each(deck,player,dealer)
    action=player_io.ask_player_action()
    while action=='H':
        player['hand'].append(deck.pop())
        value_hand=calculate_hand_value(player['hand'])
        if value_hand >21:
            print('player loos')
            value_dealer = calculate_hand_value(dealer['hand'])
            value_player = calculate_hand_value(player['hand'])
            print(value_dealer,value_player)
            return
        if value_hand==21:
            print('player won')
            print(value_hand)
            return

        print(value_hand)
        action = player_io.ask_player_action()
    action_dealer=dealer_play(deck,dealer)
    if action_dealer:
        value_player=calculate_hand_value(player['hand'])
        value_dealer = calculate_hand_value(dealer['hand'])
        if value_dealer>value_player:
            print('dealer won')
        elif value_player>value_dealer:
            print('player won')
        else:
            print('draw')
    value_dealer = calculate_hand_value(dealer['hand'])
    value_player = calculate_hand_value(player['hand'])
    print(value_dealer,value_player)




