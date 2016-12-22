from google.appengine.ext import db


#auto_now_add will add the date/time stamp when a new record is created
#auto_now will display when the item was last updated


class Art(db.Model):
    title = db.StringProperty(required = True)
    art = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)