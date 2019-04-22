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

    def__init__(self,submitted_by,pitch,category):
        self.submitted_by=submitted_by
        self.pitch=pitch
        self.category=category


class review:
    '''
    review class to allow users to comment on a pitch
    '''
    all_reviews = []

    def __init__(self,pitch,submitted_by,review):
        self.pitch=pitch
        self.submitted_by=submitted_by
        self.review=review

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





