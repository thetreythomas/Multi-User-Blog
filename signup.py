import main.Handler

class Signup(Handler):
    def get(self):
        self.render("user-signup.html")