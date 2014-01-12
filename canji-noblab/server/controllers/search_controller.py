##
# @file    search_controller.py
# @author  Hidenonu Hashikami
# @date    2014/01/06
#
# Copyright(C) 2014 hhashikami All Rights Reserved.
#
"""Controller handles routes starting with /search."""


from server.lib.bottle import Bottle, debug
from view_helper import JINJA_ENV
#from server.models.canji_model import Men, Women
#from server.models.RESOURCE_NAME import RESOURCE_NAME

bottle = Bottle()


@bottle.get('/')
def search():
	"""Display root URL of /search."""
	return JINJA_ENV.get_template('search.html').render()


@bottle.get('/detail')
def detail():
	"""Display root URL of /search/detail."""
	return JINJA_ENV.get_template('search-detail.html').render()