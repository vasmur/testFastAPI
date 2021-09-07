from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    id: int = 1
    name: str = None
    role: str = None

app = FastAPI()
login_db = []

@app.get("/login")
async def get():
	return login_db

@app.post("/login")
def add_login(user: User):
    login_db.append(user.dict())
    return login_db[-1]

@app.post("/blog/{user_id}")
def update_login(user_id: int, user: User):
    login_db[user_id] = user
    return {"message": "Post has been updated succesfully"}	

@app.delete("/blog/{user_id}")
def delete_post(user_id: int):
    login_db.pop(user_id)
    return {"message": "Post has been deleted succesfully"}