from google.appengine.ext import db
from user import User
from post import Post

class Likes(db.Model):
    user = db.ReferencePropety(User, required = True)
    post = db.ReferencePropety(Post, required = True)