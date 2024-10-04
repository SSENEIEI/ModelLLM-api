from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import requests

class JsonInout(BaseModel):
    promt: str = Field(...)



app = FastAPI()

@app.get("/")
async def root():
    return {"message":"welcome to root"}


@app.post("/testnoex")
async def test(promt_inout:JsonInout):
    prompt = {
    "prompt":"{promt_inout.promt}",
    "n_predict":256,"stop": ["</eos>"]
}    
    response = requests.post("http://llamacpp:8080/completion",json=prompt)
    return response
