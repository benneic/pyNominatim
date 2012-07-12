#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='pyNominatim',
    version='0.0.4',
    description='Open Street Map Nominatim Client',
    author='Benn Eichhorn',
    url='https://github.com/beichhor',
    packages=['pyNominatim'],
    install_requires=[
        'bunch==1.0.1',
        'requests>=0.9.1,<1.0',
        'simplejson==2.3.2',
        'python-dateutil==1.5'
    ],
    keywords='osm open street maps nominatim',
    include_package_data=True,
    zip_safe=True,
)
