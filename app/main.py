from fastapi import FastAPI
from app.api.index import api_router

app = FastAPI(title="Technical Test API")

app.include_router(api_router)


@app.get("/")
def root():
    return {"status": "ok"}
