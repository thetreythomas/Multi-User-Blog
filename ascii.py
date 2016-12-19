from handler import Handler
from databases import Art

class Ascii(Handler):
    def render_front(self, title="", art="", error=""):
        self.render("ascii.html", title=title, art=art, error=error)

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