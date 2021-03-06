from blogfiles.actions.handler import Handler
from blogfiles.models.post import Post
from blogfiles.models.user import User

from google.appengine.ext import db

def blog_key(name = 'default'):
    return db.Key.from_path('blogs', name)

class NewPost(Handler):
    def get(self):
        if self.user:
            self.render("newpost.html")
        else:
            self.redirect("/signup")

    def post(self):
        subject = self.request.get("subject")
        content = self.request.get("content").replace('\n', '<br>')
        userID = User.by_name(self.user.name)

        if subject and content and self.user:
            p = Post(parent = blog_key(),
                     subject = subject,
                     content = content,
                     user = userID)
            p.put()
            self.redirect('/blog/%s' % str(p.key().id()))
        else:
            error = "Both a Subject and Content need to be submitted. Please try again."
            self.render('newpost.html',
                        subject = subject,
                        content = content,
                        error = error)