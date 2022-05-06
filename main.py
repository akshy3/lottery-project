

from fastapi import FastAPI
# import json
import utils
app = FastAPI()

LOTTERY = ["win-win","karunya"]

@app.get("/")
def index():
    return LOTTERY


@app.get("/{name}/{serial}")
def getResults(name: str, serial: str):
    if name not in LOTTERY:
        return {"error": "Invalid lottery name"}
    serial = serial.upper()
    data = utils.getResults(name,serial)
    return data


