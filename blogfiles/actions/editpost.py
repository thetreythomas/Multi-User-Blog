from handler import Handler
from user import User
from post import Post

class EditPost(Handler):
    """Handles editing of blog posts"""
    def get(self):
        if self.user:
            post_id = self.request.get("post")
            key = ndb.Key('BlogPost', int(post_id), parent=blog_key())
            post = key.get()
            if not post:
                self.error(404)
                return
            self.render("editpost.html", subject = post.subject, content = post.content)
        else:
            self.redirect("/login")

    def post(self):
        post_id = self.request.get("post")
        key = ndb.Key('BlogPost', int(post_id), parent=blog_key())
        post = key.get()
        if post and post.author.username == self.user.username:
            subject = self.request.get("subject")
            content = self.request.get("content")
            if subject and content:
                post.subject = subject
                post.content = content
                post.put()
                time.sleep(0.1)
                self.redirect("/blog")
            else:
                error = "you need both a subject and content"
                self.render("editpost.html", subject = subject, content = content, error = error)
        else:
            self.redirect("/blog")