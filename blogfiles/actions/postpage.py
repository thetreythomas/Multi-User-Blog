from handler import Handler
import time
from blogfiles.models.post import Post
from blogfiles.models.user import User

from google.appengine.ext import db

def blog_key(name = 'default'):
    return db.Key.from_path('blogs', name)

class PostPage(Handler):
    def get(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent = blog_key())
        post = db.get(key)

        if not post:
            self.error(404)
            return

        self.render("permalink.html", post = post)

    def post(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent = blog_key())
        post = db.get(key)

        if self.user:
            if self.request.get("edit"):
                if post.user.key().id() == User.by_name(self.user.name).key().id():
                    output = self.request.get("edit")
                    self.write(output)
                    #self.redirect("/blog/%s/editpost" % str(post.key().id()))
                else:
                    edit_error = "Failed to edit post"
                    self.render("permalink.html", post = post, error = edit_error)

            if self.request.get("editButton"):
                if post.user.key().id() == User.by_name(self.user.name).key().id():
                    print self.request.get("editButton")
                    #self.write("editButton worked")
                    #self.redirect("/blog/%s/editpost" % str(post.key().id()))
                else:
                    edit_error = "Failed to edit post"
                    self.render("permalink.html", post = post, error = edit_error)

            if self.request.get("delete"):
                if post.user.key().id() == User.by_name(self.user.name).key().id():
                    db.delete(key)
                    time.sleep(0.2)
                    self.redirect("/blog")
                else:
                    delete_error = "Failed to delete post"
                    self.render("permalink.html", post = post, error = delete_error)

            if self.request.get("deleteButton"):
                if post.user.key().id() == User.by_name(self.user.name).key().id():
                    db.delete(key)
                    time.sleep(0.2)
                    self.redirect("/blog")
                else:
                    delete_error = "Failed to delete post"
                    self.render("permalink.html", post = post, error = delete_error)


        else:
            self.redirect("/blog")