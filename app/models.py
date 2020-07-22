from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

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
    comment = db.relationship("Comments", backref="user", lazy = "dynamic")

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
        categories = Category.query.all()
        return categories





class Pitch(db.Model):
    '''
    Class to create our pitch objects
    '''

    __tablename__= 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    pitch = db.Column(db.String())
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    comment = db.relationship("Comments", backref="pitches", lazy = "dynamic")
    #vote = db.relationship("Votes", backref="pitches", lazy = "dynamic")

    def save_pitches(self):
        '''
        Saving pitches
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def clear_pitches(cls):
        Pitch.all_pitches.clear()

    def get_pitches(id):
        pitches = Pitch.query.filter_by(category_id =id).all()
        return pitches

class Comments(db.Model):
    """
    Class to create comments objects
    """

    __tablename__ = 'comments'

    # add columns
    id = db.Column(db. Integer, primary_key=True)
    comment= db.Column(db.String(255))
    time_posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    pitches_id = db.Column(db.Integer, db.ForeignKey("pitches.id"))


    def save_comments(self):
        """
        Save the Comments/comments per pitch
        """
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(self, id):
        comment = Comments.query.order_by(Comments.time_posted.desc()).filter_by(pitches_id=id).all()
        return comment
