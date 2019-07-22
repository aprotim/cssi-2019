#main.py
# the import section
import webapp2
import os
import json

from google.appengine.api import urlfetch

class MainPage(webapp2.RequestHandler):
    def get(self): #for a get request
        result = urlfetch.fetch("https://opentdb.com/api.php?amount=5&category=12&difficulty=hard")

        self.response.headers['Content-Type'] = 'text/plain'
        result_data = json.loads(result.content)
        # self.response.write(result_data)
        self.response.write(result_data['results'][0]['question'])
        # self.response.write(json.dumps(result_data, indent=4))

# the app configuration section
app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
