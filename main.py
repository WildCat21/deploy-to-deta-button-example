from fastapi import FastAPI
app = FastAPI()
@app.get("/")
print("test")
