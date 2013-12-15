"""
dotter

Copyright (c) 2013, Friedrich Paetzke (f.paetzke@gmail.com)
All rights reserved.

"""
import os

from setuptools import setup, find_packages


pathname = os.path.abspath(os.path.dirname(__file__))
try:
    from orgco import convert_rst

    with open(os.path.join(pathname, 'README.org')) as org_file:
        with open(os.path.join(pathname, 'README.rst'), 'w') as rst_file:
            rst_file.write(convert_rst(org_file.read()))
except:
    print('Error converting .org')


setup(name='dotter',
      py_modules=['dotter'],
      description='Dotter is a graphviz wrapper for Python 3',
      long_description=(open('README.rst').read()),
      version='0.0.3',
      license='BSD',
      author='Friedrich Paetzke',
      author_email='f.paetzke@gmail.com',
      url='https://github.com/paetzke/dotter',
      packages=find_packages(exclude=['test*']),
      classifiers=[
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Topic :: Software Development :: Libraries',
          'Topic :: Utilities',
      ])