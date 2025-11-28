#!/usr/bin/env python3

from app import app
from models import db, Plant

with app.app_context():
    # Ensure tables exist
    db.create_all()

    print("Clearing old data...")
    Plant.query.delete()
    db.session.commit()  # Commit deletion

    print("Seeding plants...")
    plants = [
        Plant(name="Aloe", image="./images/aloe.jpg", price=11.50, is_in_stock=True),
        Plant(name="ZZ Plant", image="./images/zz-plant.jpg", price=25.98, is_in_stock=False),
        Plant(name="Fiddle Leaf Fig", image="./images/fiddle.png", price=50.0, is_in_stock=True),
        Plant(name="Snake Plant", image="./images/snake.png", price=20.0, is_in_stock=True)
    ]

    db.session.add_all(plants)
    db.session.commit()

    print("Seeding complete!")
