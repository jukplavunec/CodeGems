import logging
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from random import randint

app = FastAPI(description="It's a PRG-pattern example")

logger = logging.getLogger(__name__)


class UserIn(BaseModel):
    username: str
    user_email: str


@app.post("/user", tags=["users"])
async def create_new_user(user: UserIn):
    user_id = randint(1, 1000000)
    logger.critical(f"User {user.username}: user_id = {user_id} created")
    return RedirectResponse(url=f"/user/{user_id}", status_code=303)


@app.get("/user/{user_id}", tags=["users"])
async def get_user(user_id: int):
    logger.critical(f"User with user_id = {user_id} requested")
    return {"user_id": user_id}
