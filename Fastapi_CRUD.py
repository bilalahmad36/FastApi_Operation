from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# BaseModel with id and name
class Item(BaseModel):
    id: int
    name: str

# Fake DB (list of items)
items_db: List[Item] = []

# ------------------------
# CREATE (POST)
# ------------------------
@app.post("/items/", response_model=Item)
def create_item(item: Item):
    # check if item with same id exists
    for existing in items_db:
        if existing.id == item.id:
            raise HTTPException(status_code=400, detail="Item already exists")
    items_db.append(item)
    return item

# ------------------------
# READ (GET all)
# ------------------------
@app.get("/items/", response_model=List[Item])
def get_items():
    return items_db

# ------------------------
# READ (GET one by id)
# ------------------------
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

# ------------------------
# UPDATE (PUT)
# ------------------------
@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated_item: Item):
    for index, item in enumerate(items_db):
        if item.id == item_id:
            items_db[index] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

# ------------------------
# DELETE
# ------------------------
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for index, item in enumerate(items_db):
        if item.id == item_id:
            items_db.pop(index)
            return {"message": f"Item {item_id} deleted"}
    raise HTTPException(status_code=404, detail="Item not found")