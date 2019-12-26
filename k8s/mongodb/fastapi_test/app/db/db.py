import logging
from os import getenv

from mongoengine import connect


def connect_to_db():
    """Simple connection to MongoDB instance in cluster."""
    try:
        logging.info("connecting to db.")
        client = connect(
            db=getenv("DB"),
            username=getenv("DB_USER"),
            password=getenv("DB_PW"),
            authentication_source=getenv("DB"),
            host=getenv("DB_HOST"),
            port=27017,
        )
        logging.info("successful")
    except Exception as e:
        logging.exception("could not connect")
