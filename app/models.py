from .import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Pitch:
    '''
    Pitch class to define Pitch objects
    '''

    def __init__(self,submitted_by,pitch_name,category,upvote,downvote):
        self.submitted_by=submitted_by
        self.pitch_name=pitch_name
        self.category=category
        self.upvote=upvote
        self.downvote=downvote

        def save_pitch(self):
            db.session.add(self)
            db.session.commit()

    @classmethod
    def get_pitches(cls,id):
        pitches = Pitch.query.filter_by(pitch_id=id).all()
        return pitches


class Review:
    '''
    review class to allow users to comment on a pitch
    '''
    __tablename__ = 'reviews'
    id = db.Column(db.Integer,primary_key = True)
    Pitch = db.Column(db.String)
    submitted_by = db.Column(db.String)
    Review = db.Column(db.String)
    upvote = db.Column(db.String)
    downvote = db.Column(db.String)
    # posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    def save_review(self):
        Review.all_reviews.append(self)

    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()

    @classmethod
    def get_reviews(cls,pitch):

        response = []

        for review in cls.all_reviews:
            if review.pitch ==pitch:
                response.append(review)

        return response

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True, index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255))
    pitches=db.relationship('Pitch', backref='user', lazy="dynamic")
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
        
    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


        def verify_password(self,password):
            return check_password_hash(self.pass_secure,password)


        def save_user(self):
            db.session.add(self)
            db.session.commit()

    def __repr__(self):
        return f'User {self.username}'

class Role(db.Model):
    __tablename__ ='roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role' ,lazy= "dynamic")

    def __repr__(self):
        return f'User {self.name}'





