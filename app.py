from fastapi import FastAPI

app = FastAPI()

items = []

@app.get("/")
def root():
    return {"hello": "world!"}

@app.post("/items")
def create_item(item: str):
    items.append(items)
    return items