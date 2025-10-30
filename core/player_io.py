


def ask_player_action() -> str:
    while True:
        action=input()
        action.upper()
        if  action in ('S','H'):
            return action




