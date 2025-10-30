


def build_standard_deck() -> list[dict]:
    rank=["a","2",'3','4','5','6','7','8','9','10','j','q','k']
    suite=["h",'c','d','s']
    deck = []
    for i in rank:
        for j in suite:
            card={'rank':i,'suite':j}
            deck.append(card)
    return deck

def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:
    pass