#api_back
#convertit NL en instructions json
# recevoir la demande
# l'envoyer à api_llm
# récupérer le JSON retourné
# l'envoyer à api_agent

from fastapi import FastAPI
from pydantic import BaseModel
import requests
import json

app = FastAPI(title='API BACK')

class Query(BaseModel):
    demande: str

@app.post('/transfert')
def recup_et_transfert(request: Query ):
    reponse_llm = requests.post('http://localhost:8001/demande', json={"demande_pour_repondre": request.demande})
    actions_en_json = json.loads(reponse_llm.json())

    reponse_agent = requests.post('http://localhost:8002/execution', json=actions_en_json)
    return reponse_agent.json()

