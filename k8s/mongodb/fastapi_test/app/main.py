import json

from fastapi import FastAPI, HTTPException

from db.db import connect_to_db
from db.user_model import User

app = FastAPI()
connect_to_db()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/health", status_code=200)
def health_check():
    try:
        User.objects().first()
        return {"message": "success"}
    except Exception as e:
        # TODO e.args might not be json encodable
        raise HTTPException(status_code=400, detail=e.args)


@app.post("/user/{first_name}")
def create_user(first_name: str, last_name: str = None):
    data = {"first_name": first_name, "last_name": last_name}

    print(data)
    try:
        User(**data).save()
        return {"status": "success"}
    except Exception as e:
        return {"fail": e.args[0]}


@app.get("/user/{first_name}")
def get_user(first_name: str, last_name: str = None):
    search_user = User.objects(first_name=first_name).first()

    try:
        found_user = {
            "first_name": search_user.first_name,
            "last_name": search_user.last_name,
        }
        print(found_user)
        return {"user": found_user}
        # return {"user": json.loads(search_user.to_json())}
    except AttributeError as e:
        return {"user": None, "fail": e.args[0]}, 404
