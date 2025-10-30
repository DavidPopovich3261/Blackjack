from core import deck,game_logic


deck1=deck.build_standard_deck()
deck.shuffle_by_suit(deck1)
c=game_logic.calculate_hand_value([deck1[0]])
print(deck1)
print(c)