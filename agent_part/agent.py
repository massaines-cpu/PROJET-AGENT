from actions.fonctions_actions import LIST_OF_ACTIONS


def excecute_actions(actions_list: list[dict]):
    for a in actions_list:
        LIST_OF_ACTIONS[a["action"]](*a["parametres"])



