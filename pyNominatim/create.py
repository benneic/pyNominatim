# -*- coding: utf-8 -*-

from .api import Nominatim

def create(email=None):
    """Returns a Roamz instance."""

    return Nominatim(email=email)
