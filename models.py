from falsktest1 import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True, nullable=False)
    email = db.Column(db.String(120), unique = True, nullable=False)
    image_file = db.Column(db.String(20),  nullable=False, default='defaut.jpg') #the images will be hashed, so will the passwords xD
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref= 'author', lazy=True) #THIS KINDA RUNS A QUERRY TO LINK THE TWO CLASSE

    def __repr__(self):
        return "User('{}','{}','{}')".format(self.username , self.email , self.image_file)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    tittle = db.Column(db.String(60), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False , default=datetime.utcnow )
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return "User('{}','{}')".format(self.tittle , self.date_posted)