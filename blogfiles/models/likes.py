from user import User
from post import Post

from google.appengine.ext import db

class Likes(db.Model):
    #user = db.ReferenceProperty(User, required = True)
    #post = db.ReferenceProperty(Post, required = True)

    user = db.IntegerProperty(required = True)
    post = db.IntegerProperty(required = True)

    @classmethod
    def by_post(cls, post_id):
        likes = Likes.all().filter('post =', int(post_id))
        return likes.count()