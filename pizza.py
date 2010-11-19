from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from model import pizzaList

class PizzaHandler(webapp.RequestHandler):
	def get(self):
	  pizzaList(self)
	  
def main():
  application = webapp.WSGIApplication([('/pizza',PizzaHandler)], debug=True)
  util.run_wsgi_app(application)
  
if __name__ == '__main__':
  main()