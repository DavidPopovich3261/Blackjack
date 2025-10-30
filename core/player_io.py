


def ask_player_action() -> str:
    while True:
        action=input('Please select S or H.')
        action.upper()
        if  action in ('S','H'):
            print('jyky')
            return action




