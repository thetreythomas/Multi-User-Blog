from user import User
from post import Post

from google.appengine.ext import db

class Likes(db.Model):
    user = db.ReferenceProperty(User, required = True)
    post = db.ReferenceProperty(Post, required = True)