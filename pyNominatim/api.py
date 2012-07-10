# -*- coding: utf-8 -*-

"""
pyNominatim.api
~~~~~~~~~

This module provides a basic API interface to Open Street Map's Nominatim service.
"""
import requests
import simplejson as json
import utils

JSON='json'
HTML='html'
XML='xml'

BASE_URL = 'http://nominatim.openstreetmap.org/'

class Nominatim(object):
  """The main Roamz class."""

  def __init__(self, format=JSON, email=None):

    # Enable keep-alive and connection-pooling.
    self.session = requests.session()
    self.session.config.update({'max_retries':3})

    self._config = {
        'format' : format,
        'email' : email,
        'addressdetails' : 1
    }
    self.add_endpoints()


  def __repr__(self):
    return '<nominatim-client at 0x%x>' % (id(self))


  def add_endpoints(self):
    self.search = Search(self)
    self.reverse = Reverse(self)


  def get(self, path, **kwargs):
    url = BASE_URL + path
    params = self._config.copy()
    for (key, value) in kwargs.iteritems(): params[key] = value
    params = utils.kwargs_converter(params)
    response = self.session.get(url, params=params)
    response.raise_for_status()
    content = json.loads(response.content)
    return content



class Endpoint(object):

    def __init__(self, api):
        self.api = api


class Search(Endpoint):

    PATH = 'search'

    def __call__(self, query, limit=1):
        return self.api.get(self.PATH, q=query, limit=limit)

class Reverse(Endpoint):

    PATH = 'reverse'

    def __call__(self, longitude=0, latitude=0, zoom=18, limit=1):
        return self.api.get(self.PATH, lat=latitude, lon=longitude, zoom=zoom, limit=limit)

