from app import app, db  # Assuming your Flask app instance is named 'app' and db instance is defined there
from models import User, Car  # Importing your User and Car models

def seed_data():
    with app.app_context():  # Ensure you're within the Flask application context
        # Create some users
        user1 = User(username='john_doe', email='john@example.com', password='password1')
        user2 = User(username='jane_doe', email='jane@example.com', password='password2')
        
        db.session.add(user1)
        db.session.add(user2)
        db.session.commit()
        
        # Create some cars
        car1 = Car(model='Toyota Camry', year=2020, color='Red', price=25000.0, description='Family sedan', user=user1)
        car2 = Car(model='Honda Civic', year=2019, color='Blue', price=22000.0, description='Compact car', user=user1)
        car3 = Car(model='Ford Mustang', year=2021, color='Yellow', price=45000.0, description='Sports car', user=user2)
        
        db.session.add(car1)
        db.session.add(car2)
        db.session.add(car3)
        db.session.commit()

if __name__ == '__main__':
    seed_data()
