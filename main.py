from openai import OpenAI
from fastapi.responses import JSONResponse
client = OpenAI()
from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/{message}")
def read_root(message: str = Path(...)):
  response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
      {"role": "system", "content": message}
    ]
  )
  assistant_message_content = response.choices[0].message.content
  print(assistant_message_content)
  return JSONResponse(content=assistant_message_content)

