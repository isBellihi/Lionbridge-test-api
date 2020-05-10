from .db import db
from datetime import datetime
from datetime import datetime

class Todo(db.Document):
    title = db.StringField(required=True)
    description = db.StringField(required=True)
    status = db.StringField(required=True)
    dueDate = db.StringField()
    createdAt = db.StringField()
