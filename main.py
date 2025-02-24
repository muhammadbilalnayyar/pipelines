from fastapi import FastAPI
print("service is starting")
# Create an instance of FastAPI
app = FastAPI()

print("service is started")
# Define a route for the root ("/") endpoint
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

# Define a route for the "/items/{item_id}" endpoint
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
# This block ensures uvicorn runs only when the script is run directly
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001, reload=True)
