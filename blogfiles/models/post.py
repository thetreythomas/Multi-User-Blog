#from blogfiles.actions.handler import Handler
from google.appengine.ext import db
from user import User


#auto_now_add will add the date/time stamp when a new record is created
#auto_now will display when the item was last updated


class Post(db.Model):
    subject = db.StringProperty(required = True)
    content = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)
    last_modified = db.DateTimeProperty(auto_now = True)
    user = db.ReferenceProperty(User, required = True, collection_name = "user_posts")

    # def renderPosts(self):
    #     self._render_text = self.content.replace('\n', '<br>')
    #     return Handler().render_str('post.html', p =self)