#main.py
# the import section
import webapp2
import jinja2
import os

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# other functions should go above the handlers or in a separate file
def get_meme_url(meme_choice):
    meme_dict = {
        'classic-surprised-pikachu': 'https://i.kym-cdn.com/entries/icons/original/000/027/475/Screen_Shot_2018-10-25_at_11.02.15_AM.png',
        'shocked-pikachu': 'https://static2.thegamerimages.com/wordpress/wp-content/uploads/2017/02/pikashocked.jpg?q=50&fit=crop&w=798&h=407&dpr=1.5',
        'detective-surprised-pikachu': 'https://i.guim.co.uk/img/media/dd703cd39013271a45bc199fae6aa1ddad72faaf/0_0_2000_1200/master/2000.jpg?width=620&quality=45&auto=format&fit=max&dpr=2&s=7ce471cd741c8353f3ba5d8397805a88',
        'ketchup-loving-pikachu': 'https://static1.srcdn.com/wordpress/wp-content/uploads/Pikachu-Ketchup-e1468812509723.jpg'
        }
    return meme_dict.get(meme_choice)

# the handler section
class MainPage(webapp2.RequestHandler):
    def get(self): #for a get request
        welcome_template = JINJA_ENVIRONMENT.get_template('templates/welcome.html')
        a_variable_dict = {
            "greeting": "Howdy",
            "adjective": "amazing"
        }
        self.response.write(welcome_template.render(a_variable_dict))

    def post(self):
        self.response.write("A post request to the EnterInfoHandler")

class ShowMemeHandler(webapp2.RequestHandler):
    def get(self):
        results_template = JINJA_ENVIRONMENT.get_template('results.html')
        the_variable_dict = {
            "title_color": "red",
            "line1": "Me: Continues to watch YouTube videos with 10 minutes of battery left",
            "line2": "Laptop: *shuts off*",
            "line3": "Me:",
            "img_url": "https://cdn.drawception.com/drawings/mRTlfYTagD.png"
        }
        self.response.write(results_template.render(the_variable_dict))

    def post(self):
        # Access the user data via the form's input elements' names.
        meme_first_line = self.request.get('user-first-ln')
        meme_second_line = self.request.get('user-second-ln')
        meme_third_line = self.request.get('user-third-ln')
        meme_img_choice = self.request.get('meme-type')
        pic_url = get_meme_url(meme_img_choice)

        results_template = JINJA_ENVIRONMENT.get_template('templates/results.html')

        # Organize that user data into a dictionary.
        the_variable_dict = {
            "line1": meme_first_line,
            "line2": meme_second_line,
            "line3": meme_third_line,
            "img_url": pic_url,
        }
        self.response.write(results_template.render(the_variable_dict))

# the app configuration section
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/memeresult', ShowMemeHandler)
], debug=True)
