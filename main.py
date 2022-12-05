from fastapi import FastAPI
from v1.tweepyauth import data
app = FastAPI()

@app.get('/')
def index():
    
    return {"message": 'Hello, World!'}
