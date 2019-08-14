#!/usr/bin/env python
from setuptools import setup

from youtube_api import VERSION


setup(name='youtube_api',
      version=VERSION,
      url='https://github.com/TomoriBot/youtube-api-wrapper',
      author="Pineapple Cookie",
      author_email="pineapple.cookie.373@gmail.com",
      description="A (work in progress) Python YouTube API Wrapper.",
      long_description=open('README.rst').read(),
      keywords="YouTube, Api",
      license=open('LICENSE').read(),
      platforms=['linux'],
      packages=('youtube_api', ),
      include_package_data=True,
      # See http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Apache Software License',
          'Operating System :: Unix',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries :: Python Modules'],
      install_requires=[
          'requests>=2.6'],
      )
