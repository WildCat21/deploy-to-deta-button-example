import os
from deta import Deta
from fastapi import FastAPI

app = FastAPI()
@app.get("/")

def index():
  deta = Deta("api_key")
  users = deta.Base("tesst")
  users.insert({"key": "test", "bann": "0", })
