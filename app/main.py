from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello_world():
    return {"SPCN25": "OK"}
