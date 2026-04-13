#api
from fastapi import FastAPI
from pydantic import BaseModel
from agent import excecute_actions
#recoit qqch en json et le transmet a agent

app = FastAPI()

class Actions(BaseModel):
    action: str
    parametres: list

class Liste(BaseModel):
    liste_des_actions: list[Actions]


@app.post("/execution")
def jsp(reception: Liste):
    conversion_actions_en_dictionnaire = [a.model_dump() for a in reception.liste_des_actions]
    excecute_actions(conversion_actions_en_dictionnaire)

