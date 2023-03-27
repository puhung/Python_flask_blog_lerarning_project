from datetime import datetime
from puppycompanyblog import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# allow us to check if users are authenticated
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin): # This allow the UserMixin functionality
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    profile_image = db.Column(db.String(64), nullable=False, default='default_profile.png') # a link to the image file. nullable=False means all users need to have image 
    email = db.Column(db.String(64),unique=True,index=True) 
    username = db.Column(db.String(64),unique=True,index=True)
    password_hash = db.Column(db.String(128))

    # backref describe this relationship and can be called in templates
    posts = db.relationship('BlogPost',backref='author', lazy=True)

    def __init__(self,email,username,password) :
        self.email=email
        self.username=username
        self.password_hash=generate_password_hash(password)

    # Can be used in login view
    def check_password(self,password):
        return check_password_hash(self.password_hash,password)
    
    def __repr__(self):
        return "Username {}".format(self.username)
    

class BlogPost(db.Model):
    users = db.relationship(User)

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False) # users is the table name, id is the attribute of that table
    date = db.Column(db.DateTime, nullable=False,default=datetime.utcnow) #  nullable=False -> every blog post needs a date time
    title = db.Column(db.String(140),nullable=False)
    text = db.Column(db.Text,nullable=False)

    def __init__(self,title,text,user_id):
        self.title = title
        self.text=text
        self.user_id=user_id

    def __repr__(self):
        return "Post ID: {} -- Date: {self.date} --- {self.title}".format(self.id, self.date)