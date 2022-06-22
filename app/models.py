from app import db, login
from flask_login import UserMixin
from datetime import datetime as dt
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String, unique=True, index=True)
    password = db.Column(db.String)
    created_on = db.Column(db.DateTime, default=dt.utcnow)
    hive = db.relationship('Hive',
                    secondary = '',
                    backref = 'users',
                    lazy = 'dynamic'
                    )

    def __repr__(self):
        return f'<User: {self.email} | {self.id}>'

    def __str__(self):
        return f'<User: {self.email} | {self.first_name} {self.last_name}>'

    def hash_password(self, original_password):
        return generate_password_hash(original_password)

    def check_hashed_password(self, login_password):
        return check_password_hash(self.password, login_password)

    def from_dict(self, data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = self.hash_password(data['password'])
        self.hive = data['hive']
        
    def save(self):
        db.session.add(self)
        db.session.commit()

    def add_hive(self, hive):
        self.hive.append(hive)
        db.session.commit()

    def remove_hive(self, hive):
        self.hive.remove(hive)
        db.session.commit()

    

class Hive (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    hive_name = db.Column(db.String)
    queen = db.Column(db.String)
    health = db.Column(db.String)
    temperment = db.Column(db.String)
    notes = db.Column(db.Text)

    def save(self):
        db.session.add(self)
        db.session.commit()


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
