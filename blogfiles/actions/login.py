from blogfiles.actions.handler import Handler


class Login(Handler):
    def get(self):
        self.render('login.html')