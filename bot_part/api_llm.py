#api_lmm
from fastapi import FastAPI
from openai import OpenAI
from pydantic import BaseModel
import os

app = FastAPI()

gpt = OpenAI(api_key = os.getenv('API_KEY_AZURE'),base_url= os.getenv('URL_AZURE'))

class Demande(BaseModel):
    demande_pour_repondre: str

#endpoint doit recevoir une demande str et retourner la réponse du LLM.

@app.post('/demande')
def demande_llm(request: Demande):
    demande = request.demande_pour_repondre
    reponse = gpt.chat.completions.create(
        model='gpt-5.1-chat',
        messages=[
            {'role': 'system', 'content': 'tu es un agent, réponds uniquement en français'},
            {'role': 'user', 'content': demande }])
    return reponse.choices[0].message.content