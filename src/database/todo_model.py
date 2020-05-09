from .db import db
from datetime import datetime


class Todo(db.Document):
    title = db.StringField(required=True, unique=True)
    description = db.ListField(db.StringField(), required=True)
    status = db.ListField(db.StringField(), required=True)
    createdAt = db.DateTimeField(default=datetime.utcnow)
