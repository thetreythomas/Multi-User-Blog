from blogfiles.actions.handler import Handler

class Logout(Handler):
    def get(self):
        self.logout()
        self.redirect('/blog')