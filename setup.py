#!/usr/bin/env python
from setuptools import setup, find_packages


try:
    import oscar
except ImportError:
    # Oscar not installed
    pass


setup(name='django-oscar-rosetta',
      version=0.01,
      url='https://github.com/scaryclam/django-oscar-rosetta',
      author="Becky Lewis",
      author_email="github@scaryclam.co.uk",
      description="rosetta module for django-oscar",
      long_description=open('README.rst').read(),
      keywords="Rosetta, Django, Oscar",
      license='MIT',
      platforms=['linux'],
      packages=find_packages(exclude=['tests*']),
      include_package_data=True,
      # See http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'License :: MIT',
          'Operating System :: Unix',
          'Programming Language :: Python',
          'Topic :: Other/Nonlisted Topic'],
      install_requires=[
          'django-rosetta>=0.7',
      )

