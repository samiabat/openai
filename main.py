from openai import OpenAI
from fastapi.responses import JSONResponse
client = OpenAI()
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
  response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "Who won the world series in 2020?"},
      {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
      {"role": "user", "content": "Where was it played?"}
    ]
  )
  return JSONResponse(content=str(response))

