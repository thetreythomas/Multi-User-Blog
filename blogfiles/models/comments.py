from user import User
from post import Post

from google.appengine.ext import db

class Comments(db.Model):
    author = db.ReferenceProperty(User, required = True)
    post = db.ReferenceProperty(Post, required = True)
    content = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)

    @classmethod
    def get_comments_by_id(cls, id):
        comments = Comments.all().filter("post =", id).order('created')
        return comments