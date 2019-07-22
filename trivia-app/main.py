#main.py
# the import section
import webapp2
import os

from google.appengine.api import urlfetch

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self): #for a get request
        self.response.write("Who's ready for some trivia?")

# the app configuration section
app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
