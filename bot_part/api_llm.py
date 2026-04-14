#api_lmm
from fastapi import FastAPI
from openai import OpenAI
import os

app = FastAPI()

gpt = OpenAI(api_key = os.getenv('API_KEY_AZURE'),base_url= os.getenv('URL_AZURE'))

reponse = gpt.chat.completions.create(
    model='gpt-5.1-chat',
    messages=[
        {'role': 'system', 'content': 'tu es un agent, réponds uniquement en français'},
        {'role': 'user', 'content': 'demande '}
    ]
)
texte = reponse.choices[0].message.content