from app import db

class Vehicle(db.Model):
	__abstract__ = True
	id = db.Column(db.Integer, primary_key=True)
	type = db.Column(db.String(100))

class Cars(Vehicle):
    __tablename__ = 'cars'
    id = db.Column(db.Integer, primary_key=True)
    manufacturer = db.Column(db.String(100))
    model = db.Column(db.String(100))
    price = db.Column(db.String(100))
    year = db.Column(db.String(100))
