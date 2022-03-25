from . import db
from datetime import datetime


class Food_Item(db.Model):

    __tablename__ = 'Food Items'

    id = db.Column(db.Integer, primary_key= True)

    name = db.Column(db.String(50), nullable = False)

    content = db.Column(db.String(200), nullable = False)

    date_created = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return '<Food Item %r>' % self.id