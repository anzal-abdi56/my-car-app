from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

    
class User(db.Model, SerializerMixin):
    __tablename__="users"

    serialize_rules=('-car-users')

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    cars = db.relationship('Car', backref='user')


    def __repr__(self):
        return f"<User {self.username}>"
    


class Car(db.Model, SerializerMixin):
    __tablename__ ='cars'

    serialize_rules=('-user-cars')

    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    color = db.Column(db.String(20))
    price = db.Column(db.Float)
    description = db.Column(db.Text)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


