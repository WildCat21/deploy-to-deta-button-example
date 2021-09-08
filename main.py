import os, deta
from fastapi import FastAPI

app = FastAPI()
@app.get("/")

def index():
  print("test")
  return False
