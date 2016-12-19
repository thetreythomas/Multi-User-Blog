from handler import Handler
from databases import Post

from google.appengine.ext import db

def blog_key(name = 'default'):
    return db.Key.from_path('blogs', name)

class BlogFront(Handler):
    def get(self):
        posts = Post.all().order('-created')
        #GQL for the above would be
        # db.GqlQuery(SELECT * FROM Post ORDER BY created DESC LIMIT 10)
        self.render('blog.html', posts = posts)

class PostPage(Handler):
    def get(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent = blog_key())
        post = db.get(key)

        if not post:
            self.error(404)
            return

        self.render("permalink.html", post = post)

class NewPost(Handler):
    def get(self):
        self.render("newpost.html")

    def post(self):
        subject = self.request.get("subject")
        content = self.request.get("content")
