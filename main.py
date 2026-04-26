from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return{"message":"this is a job application tracker"}