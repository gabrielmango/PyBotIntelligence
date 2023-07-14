from fastapi import FastAPI
from chatbot import conversa

app = FastAPI()

@app.get('/')
async def root(): 
    return {"message": "Working"}

@app.get('/{pergunta}')
def chat_conversa(pergunta): 
    resposta = conversa(pergunta)
    return {resposta}