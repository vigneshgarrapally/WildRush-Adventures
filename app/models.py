"""
This module contains the models for the Flask application.
"""
from app import db, app
from flask_login import UserMixin


class User(db.Model, UserMixin):
    """
    This class represents the User table in the database.
    """

    email = db.Column(db.String(120), index=True, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f"<User {self.email}>"

    # Required methods for Flask-Login
    def get_id(self):
        return self.email

    @staticmethod
    def get(email):
        return User.query.get(email)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Lead(db.Model):
    """
    This class represents the Contact table in the database.
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)
    consent = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"<Contact {self.name}>"


# Create the database tables
with app.app_context():
    db.create_all()
