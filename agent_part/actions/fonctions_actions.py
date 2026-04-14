import os

#print hello

def hello():
    ''' cette fonction sert à print 'hello' un fichier dans le termninal'''

    print("hello")
#créer un fichier

def creer_un_fichier(nom):
    ''' cette fonction sert à créer un fichier dans le projet'''

    with open(nom, 'w+'):
        pass
#creer un dossier

def creer_un_dossier(nom):
    ''' cette fonction sert à créer un dossier dans le projet'''

    try:
        os.mkdir(nom)
    except FileExistsError:
        print(f"'{nom}' existe déjà")

#renommer fichier
def renommer_fichier(ancien_nom, nouveau_nom ):
    ''' cette fonction sert à créer à renommer un fichier dans le projet'''
    os.rename(ancien_nom, nouveau_nom)

#lire le contenu fichier

def lire_contenu_fichier(nom):
    ''' cette fonction sert à lire le contenu d'un fichier dans le projet'''
    with open(nom, 'r') as f:
        contenu = f.read()
        print(contenu)



LIST_OF_ACTIONS = {
    "creer_un_fichier": creer_un_fichier,
    "hello": hello,
    'creer_un_dossier': creer_un_dossier,
    'lire_contenu_fichier': lire_contenu_fichier,
    'renommer_fichier': renommer_fichier
}

liste_de_description = []
for k, v in LIST_OF_ACTIONS.items():
    description = k + ': ' + v.__doc__
    liste_de_description.append(description)

description_finale = '\n'.join(liste_de_description)

print(liste_de_description)