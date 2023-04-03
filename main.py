from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/users")
async def get_users():
	with open("users.json","r") as file:
		users = json.load(file)
	return users