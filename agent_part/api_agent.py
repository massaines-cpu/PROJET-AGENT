#api
from fastapi import FastAPI
from pydantic import BaseModel
from agent import excecute_actions
from actions.fonctions_actions import LIST_OF_ACTIONS

#recoit qqch en json et le transmet a agent

app = FastAPI(title="API AGENT")

class Actions(BaseModel):
    action: str
    parametres: list

class Liste(BaseModel):
    liste_des_actions: list[Actions]

liste_de_description = []
for k, v in LIST_OF_ACTIONS.items():
    description = k + ': ' + v.__doc__
    liste_de_description.append(description)

description_finale = '\n'.join(liste_de_description)

@app.post("/execution", description=description_finale)
def execution_agent(reception: Liste):
    conversion_actions_en_dictionnaire = [a.model_dump() for a in reception.liste_des_actions]
    excecute_actions(conversion_actions_en_dictionnaire)

