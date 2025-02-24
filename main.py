from fastapi import FastAPI

# Create an instance of FastAPI
app = FastAPI()

# Define a route for the root ("/") endpoint
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

# Define a route for the "/items/{item_id}" endpoint
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
