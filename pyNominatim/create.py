# -*- coding: utf-8 -*-

from .api import Nominatim, JSON

def create(format=JSON, email=None, addressdetails=False):
    """Returns a Roamz instance."""

    return Nominatim(format=format, email=email, addressdetails=addressdetails)
