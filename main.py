from fastapi import FastAPI
from fastapi.testclient import TestClient
import uvicorn

app = FastAPI()


@app.get("/")
async def read_main():
    return {"msg": "Hello Wrld"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)