from handler import Handler
import time
from blogfiles.models.post import Post
from blogfiles.models.user import User
from blogfiles.models.likes import Likes
from blogfiles.models.comments import Comments

from google.appengine.ext import db

def blog_key(name = 'default'):
    return db.Key.from_path('blogs', name)

class PostPage(Handler):
    def get(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent = blog_key())
        post = db.get(key)
        likes = Likes.by_post(post_id)

        comments = Comments.get_comments_by_id(post)

        if not post:
            self.error(404)
            return

        self.render("permalink.html", post = post, comments = comments, likes = likes)

    def post(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent = blog_key())
        post = db.get(key)

        comments = Comments.get_comments_by_id(post)

        if self.user:
            if self.request.get("edit"):
                print "\n POST request for edit \n"
                if post.user.key().id() == User.by_name(self.user.name).key().id():
                    self.redirect("/blog/%s/editpost" % str(post.key().id()))
                else:
                    edit_error = "Failed to edit post"
                    self.render("permalink.html", post = post, error = edit_error)


            if self.request.get("delete"):
                print "\n POST request for delete \n"
                if post.user.key().id() == User.by_name(self.user.name).key().id():
                    db.delete(key)
                    time.sleep(0.2)
                    self.redirect("/blog")
                else:
                    delete_error = "Failed to delete post"
                    self.render("permalink.html", post = post, error = delete_error)


            if self.request.get("like"):
                print "\n POST request for like \n"
                if post.user.key().id() == User.by_name(self.user.name).key().id():
                    like_error = "You cannot like your own post"
                    self.render("permalink.html", post = post, error = like_error)
                else:
                    #like = Likes(post = post, user = User.by_name(self.user.name))
                    like = Likes(post = int(post_id), user = self.user.key().id())
                    like.put()
                    time.sleep(0.2)
                    self.redirect("/blog/%s" % str(post.key().id()))


            if self.request.get("comment"):
                print "\n POST request for comment \n"
                content = self.request.get("content")
                if content:
                    newComment = Comments(author = User.by_name(self.user.name), post = post, content = content)
                    newComment.put()
                    time.sleep(0.2)
                    self.redirect("/blog/%s" % str(post.key().id()))
                else:
                    comment_error = "Please enter some text if you would like to leave a comment."
                    self.render("permalink.html", post = post, comment_error = comment_error)


            if self.request.get("deleteComment"):
                print "\n POST request for delete comment \n"
                commentToDeleteID = self.request.get("commentToDelete")
                comment = Comments.get_by_id(int(commentToDeleteID))
                if comment.author.name == self.user.name:
                    db.delete(comment)
                    time.sleep(0.2)
                    self.redirect("/blog/%s" % str(post.key().id()))
                else:
                    delete_error = "You are not able to delete this comment."
                    self.render("permalink.html", post = post, delete_error = comment_error)


            if self.request.get("edit_comment"):
                print "\n POST request for edit comment \n"
                comment = self.request.get("comment.key")
                self.redirect('/blog/%s/%s/editcomment' % (str(post.key().id()), str(comment.key().id())) )


        else:
            self.redirect("/blog")















