from fastapi import FastAPI

app = FastAPI(title="JEE Sense AI")


@app.get("/")
def root():
    return {"message": "JEE Sense AI API is running"}