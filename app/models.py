from . import db
from datetime import datetime

class Properties(db.Model):
    __tablename__ = 'properties'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    nofrooms = db.Column(db.String(80), nullable=False)
    nofbrooms = db.Column(db.String(80), nullable=False)
    location = db.Column(db.String(80), nullable=False)
    image = db.Column(db.String(80), nullable=False)
    price = db.Column(db.String(80), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.now)  # Changed to default=datetime.now
    description = db.Column(db.String(80), nullable=False)
    type = db.Column(db.String(80), nullable=False)
