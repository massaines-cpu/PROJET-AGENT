import os

#créer un fichier

def creer_un_fichier(nom):
    with open(nom, 'w+'):
        pass

#creer un dossier

def creer_un_dossier(nom):
    try:
        os.mkdir(nom)
    except FileExistsError:
        print(f"'{nom}' existe déjà")

#renommer fichier
def renommer_fichier(ancien_nom, nouveau_nom ):
    os.rename(ancien_nom, nouveau_nom)

def hello():
    print("hello")

#lire le contenu fichier

def lire_contenu_fichier(nom):
    with open(nom, 'r') as f:
        contenu = f.read()
        print(contenu)
    # lire = open(nom, 'r')
    # contenu = lire.read()
    # print(contenu)


