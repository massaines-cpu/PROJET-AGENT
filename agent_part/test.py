from agent_part.agent import excecute_actions

liste_test = [
    {
        "action": "hello",
        "parametres": []
    },
    {
        "action": "creer_un_fichier",
        "parametres": ["no_help"]
    },
{
        "action": "creer_un_dossier",
        "parametres": ["the_boys"]
    },
{
        "action": "renommer_fichier",
        "parametres": ["no_help", 'breaking_news']
    },
    {'action': 'lire_contenu_fichier',
     'parametres': ['pioupiou.txt']}
]
excecute_actions(liste_test)
