from handler import Handler
import time
from blogfiles.models.post import Post
from blogfiles.models.user import User
from blogfiles.models.comments import Comments

from google.appengine.ext import db

def blog_key(name = 'default'):
    return db.Key.from_path('blogs', name)

class EditComment(Handler):
    def get(self, postID, commentID):
        key = db.Key.from_path('Post', int(postID), parent = blog_key())
        post = db.get(key)

        comment = Comments.get_by_id(int(commentID))
        if comment:
            if comment.author.name == self.user.name:
                self.render("editcomment.html", comment = comment)
            else:
                self.redirect("/blog/%s" % str(post.key().id()))

    def post(self, postID, commentID):
        key = db.Key.from_path('Post', int(postID), parent = blog_key())
        post = db.get(key)

        if self.request.get("save"):
            comment = Comments.get_by_id(int(commentID))
            if comment.author.name == self.user.name:
                comment.content = self.request.get("content")
                comment.put()
                time.sleep(0.2)
                self.redirect("/blog/%s" % str(post.key().id()))
            else:
                save_error = "Only the author of the comment can make changes."
                self.render("editcomment.html", comment = comment, save_error = save_error)

        if self.request.get("cancel"):
            self.redirect("/blog/%s" % str(post.key().id()))