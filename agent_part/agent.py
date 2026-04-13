from agent_part.actions.liste_des_actions import LIST_OF_ACTIONS


def excecute_actions(actions_list: list[dict]):
    for call in actions_list:
        LIST_OF_ACTIONS[call["action"]](*call["params"])