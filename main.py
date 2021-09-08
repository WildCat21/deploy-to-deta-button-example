import os
from deta import Deta
from fastapi import FastAPI

app = FastAPI()
@app.get("/")

def index():
  deta = Deta("a0nx7pgk_CAsXSD5UjJsWT8xj9nPSAb14xduJ1fUR")
  users = deta.Base("tesst")
  users.insert({"key": "test", "bann": "0", })
