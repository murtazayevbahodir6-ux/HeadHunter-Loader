import os
from data.config import HOST, USER, PASSWORD, DB
import logging
from db.database import Database


db = Database(
    host=HOST, user=USER, password=PASSWORD, db=DB
)
