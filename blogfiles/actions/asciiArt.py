from blogfiles.actions.handler import Handler
from blogfiles.models.art import Art

# This is needed for the db queries and inserts
from google.appengine.ext import db

class Ascii(Handler):
    def render_front(self, title="", art="", error=""):
        arts = db.GqlQuery("SELECT * FROM Art ORDER BY created DESC")

        self.render("ascii.html", title=title, art=art, error=error, arts = arts)

    def get(self):
        self.render_front()

    def post(self):
        title = self.request.get("title")
        art = self.request.get("art")

        if title and art:
            #self.write("Thank you. Your /ascii/ art has been submitted.")
            a = Art(title = title, art = art)
            a.put()

            self.redirect("/ascii")
        else:
            error = "We need both a title and some artwork!"
            self.render_front(title, art, error)