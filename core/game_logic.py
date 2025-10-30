



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
    pass



def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    pass