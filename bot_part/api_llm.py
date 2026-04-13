from fastapi import FastAPI
from openai import OpenAI
import os

app = FastAPI()

gpt = OpenAI(api_key = os.getenv('API_KEY_AZURE'),base_url= os.getenv('URL_AZURE'))