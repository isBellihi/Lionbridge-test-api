from .db import db
from datetime import datetime


class Todo(db.Document):
    title = db.StringField(required=True)
    description = db.StringField(required=True)
    status = db.StringField(required=True)
    dueDate = db.DateTimeField(default=datetime.utcnow)
    createdAt = db.DateTimeField(default=datetime.utcnow)
