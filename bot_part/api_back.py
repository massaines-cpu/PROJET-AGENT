#convertit NL en instructions json
#api_back
from fastapi import FastAPI
from openai import BaseModel

app = FastAPI(title='API BACK')

SWAGGER = './agent_part/swagger.json'
class Query(BaseModel):
    demande: str
    reponse: str

@app.post('/vers_LLM', description=SWAGGER)
def vers_LLM(nl: ):
    pass

@app.post('/vers_agent')
def vers_agent(reponse_llm:):
    pass