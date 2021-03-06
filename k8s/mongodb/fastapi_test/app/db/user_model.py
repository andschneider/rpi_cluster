from mongoengine import Document, StringField


class User(Document):
    first_name = StringField(required=True)
    last_name = StringField(default="")

    meta = {"collection": "users"}
