from fastapi import FastAPI
from pydantic import BaseModel

from agent_part.agent import excecute_actions

#recoit qqch en json et le transmet a agent

app = FastAPI()

class Actions(BaseModel):
    action: str
    parametres: list

@app.post("/execution")
def exe(les_actions: Actions):
    action = les_actions.action
    parametres = les_actions.parametres
