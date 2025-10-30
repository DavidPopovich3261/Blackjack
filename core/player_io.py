


def ask_player_action() -> str:
    while True:
        action=input('Please select S or H.')
        if  action in ('S','H'):
            return action




