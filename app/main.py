# app/main.py
from fastapi import FastAPI, HTTPException, status
from .schemas import User

app = FastAPI()
users: list[User] = []

@app.get("/api/users")
def get_users():
    return users

@app.get("/api/users/{user_id}")
def get_user(user_id: int):
    for u in users:
        if u.user_id == user_id:
            return u
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

@app.post("/api/users", status_code=status.HTTP_201_CREATED)
def add_user(user: User):
    if any(u.user_id == user.user_id for u in users):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="user_id already exists")
    users.append(user)
    return user

@app.put("/api/users/update/{user_id}", status_code=status.HTTP_201_CREATED)
#Here updated_user is expected to be a User object, and would be populated from the request body
def update_user(user_id: int, updated_user: User):
    #Here I use enumerate function to loop over the users list and get the position (index) and the user object at that position to update in place
    for index, u in enumerate(users):
        if u.user_id == user_id:
            #With updated_user, I can replace it with the user object at position (index)
            users[index] = updated_user
            return updated_user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

@app.delete("/app/users/delete/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):
    for u in users:
        if u.user_id == user_id:
            #.remove() function to remove the object
            users.remove(u)
            return u
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

#Prints a status
@app.get("/health")
def health():
    return {"status": "ok"}