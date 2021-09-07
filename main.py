import os
from fastapi import FastAPI

app = FastAPI()
@app.get("/")

def index():
  print("tes")
  return
