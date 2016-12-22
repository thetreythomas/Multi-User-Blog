from blogfiles.actions.handler import Handler
from blogfiles.models.post import Post
from blogfiles.actions.postpage import PostPage

from google.appengine.ext import db

def blog_key(name = 'default'):
    return db.Key.from_path('blogs', name)

class BlogFront(Handler):
    def get(self):
        posts = Post.all().order('-created')
        #GQL for the above would be
        # db.GqlQuery(SELECT * FROM Post ORDER BY created DESC LIMIT 10)
        self.render('blog.html', posts = posts)