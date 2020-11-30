from app import app
from app import db

class Icon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    IconTitle = db.Column(db.String(255),  nullable=False)
    IconText = db.Column(db.String(255),  nullable=False)

    