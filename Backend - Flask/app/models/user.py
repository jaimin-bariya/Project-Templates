
from datetime import datetime
# from database import db # Can trigger Circular Importing 
from app.database import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True )
    f_name = db.Column(db.String(30), nullable=False)
    l_name = db.Column(db.String(30), nullable=False)
    password = db.Column(db.Text, nullable=False)  # 🔥 Store hashed passwords
    city = db.Column(db.String(30), nullable=True)
    state = db.Column(db.String(50), nullable=True)
    zip = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())  # 🔥 Auto timestamp


    def __repr__(self):
        return f'<User {self.f_name}>'
    

    # We are using this methods so while retriving data, this helps
    def to_dict(self):
        return {
            "id": self.id,
            "f_name": self.f_name,  
            "l_name": self.l_name,
            "city": self.city,
            "state": self.state,
            "zip": self.zip,
            "created_at": self.created_at.isoformat() if self.created_at else None  # 🔥 Converts datetime to string
        }

