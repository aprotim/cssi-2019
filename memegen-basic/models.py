from google.appengine.ext import ndb

class Meme(ndb.Model):
    image_url = ndb.StringProperty(required=True)
    top_text = ndb.StringProperty()
    top_text = ndb.StringProperty()
    middle_text = ndb.StringProperty()
