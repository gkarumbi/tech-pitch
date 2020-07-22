from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__= 'users'
    id = db.Column(db.Integer,primary_key= True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    password_hash = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    pitches = db.relationship("Pitch", backref="user", lazy = "dynamic")
    comment = db.relationship("Comments", backref="user", lazy = "dynami

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)
    


    def __repr__(self):
        return f'User {self.username}'

class Category(db.Model):
    __tablename__= 'categories'

    #Columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))

    #save category
    def save_category(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_categories(cls):
        categories = PitchCategory.query.all()
        return categories





class Pitch:
    '''
    Class to create our pitch objects
    '''

    all_pitches = []

    def __init__(self, category, title,idea,owner):
        self.category = category
        self.title = title
        self.idea = idea
        self.owner = owner

    def save_pitches(self):
        Pitch.all_pitches.append(self)

    @classmethod
    def clear_pitches(cls):
        Pitch.all_pitches.clear()

