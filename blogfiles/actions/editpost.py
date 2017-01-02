from handler import Handler
import time
from blogfiles.models.post import Post
from blogfiles.models.user import User

from google.appengine.ext import db

def blog_key(name = 'default'):
    return db.Key.from_path('blogs', name)

class EditPost(Handler):
    def get(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent = blog_key())
        post = db.get(key)

        if self.user:
            if post.user.key().id() == User.by_name(self.user.name).key().id():
                self.render("editpost.html", post = post)
            else:
                self.write("You are only able to Edit and Delete your own blog posts.")
        else:
            self.redirect("/blog")

    def post(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent = blog_key())
        post = db.get(key)

        if self.request.get("save"):
            subject = self.request.get("subject")
            content = self.request.get("content").replace('\n', '<br>')

            if post.user.key().id() == User.by_name(self.user.name).key().id():
                if subject and content:
                    post.subject = subject
                    post.content = content
                    post.put()
                    time.sleep(0.2)
                    self.redirect('/blog/%s' % str(post.key().id()))
                else:
                    error = "Both a Subject and Content need to be submitted. Please try again."
                    self.render('editpost.html', subject = subject, content = content, error = error)

            else:
                self.write("You are only able to Edit and Delete your own blog posts.")
        elif self.request.get("cancel"):
            self.redirect('/blog/%s' % str(post.key().id()))