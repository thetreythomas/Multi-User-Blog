from handler import Handler #, PostPage
from blogfiles.models import Post

from google.appengine.ext import db

def blog_key(name = 'default'):
    return db.Key.from_path('blogs', name)

class BlogFront(Handler):
    def get(self):
        posts = Post.all().order('-created')
        #GQL for the above would be
        # db.GqlQuery(SELECT * FROM Post ORDER BY created DESC LIMIT 10)
        self.render('blog.html', posts = posts)