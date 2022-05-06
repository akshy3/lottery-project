

from fastapi import FastAPI
import json
app = FastAPI()

with open("lotteries.json") as file:
    data = json.load(file)
@app.get("/")
def read_root():
    return data


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}

