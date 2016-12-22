from blogfiles.actions.signup import Signup

class Register(Signup):
    def done(self):
        #This will be a check to see if the username already exists
        u = User.by_name(self.username)
        if u:
            msg = 'That user already exists. Please enter a different username.'
            self.render('user-signup.html', error_username = msg)
        else:
            u = User.register(self.username, self.password, self.email)
            u.put()

            self.login(u)
            self.redirect('/blog')