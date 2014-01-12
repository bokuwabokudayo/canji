##
# @file    main.py
# @author  Hidenonu Hashikami
# @date    2014/01/04
#
# Copyright(C) 2014 hhashikami All Rights Reserved.
#
"""Main.py is the top level script.
Loads the Bottle framework and mounts controllers.  Also adds a custom error handler.
"""


# import the Bottle framework
from server.lib.bottle import Bottle, debug
from server.controllers.view_helper import JINJA_ENV
# TODO: name and list your controllers here so their routes become accessible.
from server.controllers import RESOURCE_NAME_controller
from server.controllers import search_controller

# Run the Bottle wsgi application. We don't need to call run() since our
# application is embedded within an App Engine WSGI application server.
bottle = Bottle()

# Mount a new instance of bottle for each controller and URL prefix.
# TODO: Change 'RESOURCE_NAME' and add new controller references
bottle.mount("/RESOURCE_NAME", RESOURCE_NAME_controller.bottle)
bottle.mount("/search", search_controller.bottle)




#temporary
@bottle.route('/talk')
def talk():
  return JINJA_ENV.get_template('talk.html').render()
@bottle.route('/mypage')
def mypage():
  return JINJA_ENV.get_template('mypage.html').render()
@bottle.route('/footstep')
def footstep():
  return JINJA_ENV.get_template('footstep.html').render()
@bottle.route('/crush')
def crush():
  return JINJA_ENV.get_template('crush.html').render()




@bottle.route('/')
def home():
  """ Return search at application root URL"""
  return JINJA_ENV.get_template('search.html').render()

#hierarchy one level down of root url without serach etc.
@bottle.get('/about')
def about():
  """Display settlement view."""
  return JINJA_ENV.get_template('about.html').render()

@bottle.get('/guide')
def guide():
  """Display guide view."""
  return JINJA_ENV.get_template('guide.html').render()

@bottle.get('/help')
def help():
  """Display help view."""
  return JINJA_ENV.get_template('help.html').render()

@bottle.get('/safe')
def safe():
  """Display safe view."""
  return JINJA_ENV.get_template('safe.html').render()

@bottle.get('/security')
def security():
  """Display security view."""
  return JINJA_ENV.get_template('security.html').render()

@bottle.get('/terms')
def terms():
  """Display terms view."""
  return JINJA_ENV.get_template('terms.html').render()

@bottle.get('/privacy')
def privacy():
  """Display privacy view."""
  return JINJA_ENV.get_template('privacy.html').render()

@bottle.get('/contact')
def contact():
  """Display contact view."""
  return JINJA_ENV.get_template('contact.html').render()

@bottle.get('/deal')
def deal():
  """Display deal view."""
  return JINJA_ENV.get_template('deal.html').render()

@bottle.get('/settlement')
def settlement():
  """Display settlement view."""
  return JINJA_ENV.get_template('settlement.html').render()


# Error
@bottle.error(404)
def error_404(error):
  """Return a custom 404 error."""
  return 'Sorry, Nothing at this URL.'