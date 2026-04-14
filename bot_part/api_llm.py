#api_lmm
#endpoint doit recevoir une demande str et retourner la réponse du LLM.

from fastapi import FastAPI
from openai import OpenAI
from pydantic import BaseModel
from dotenv import load_dotenv

import os

app = FastAPI(title='API LLM')
load_dotenv()
gpt = OpenAI(api_key = os.getenv('API_KEY_AZURE'),base_url= os.getenv('URL_AZURE'))
print(os.getenv('API_KEY_AZURE'))
print(os.getenv('URL_AZURE'))
class Demande(BaseModel):
    demande_pour_repondre: str

direction = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(direction, '../agent_part/swagger.json'), 'r') as f:
    contenu = f.read()

@app.post('/demande')
def demande_llm(request: Demande):
    demande = request.demande_pour_repondre
    reponse = gpt.chat.completions.create(
        model='gpt-5.1-chat',
        messages=[
            {'role': 'system', 'content': f'''Tu es un agent. À partir de la demande utilisateur, 
            réponds UNIQUEMENT en JSON avec ce format :
            
            {{"liste_des_actions": [{{"action": "nom_action", "parametres": ["param1"]}}]}}
            Voici les actions disponibles : {contenu}'''},

            {'role': 'user', 'content': demande}])
    return reponse.choices[0].message.content