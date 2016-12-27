from blogfiles.actions.handler import Handler
from blogfiles.models.user import User


class Login(Handler):
    def get(self):
        self.render('login.html')

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')

        u = User.login(username, password)
        if u:
            self.login(u)
            self.redirect('/welcome?username=' + username)
            #self.redirect('/blog')
        else:
            msg = 'Invalid Login'
            self.render('login.html', error = msg)