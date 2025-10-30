from core import deck,game_logic

if __name__ == "__main__":

    deck1=deck.build_standard_deck()
    deck.shuffle_by_suit(deck1)
    player = {"hand": []}
    dealer = {"hand": []}
    game_logic.run_full_game(deck1,player,dealer)
