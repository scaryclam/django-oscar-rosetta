django-oscar-rosetta
====================

This is an extension for the django-oscar e-commerce framework. It adds rosetta into the dashboard so that
it looks more native and doesn't require translators or translation maintainers to access the django admin.

Installation
============

 - pip install from github
 - Add oscar_rosetta into your installed apps
 - In your urls.py add

::
  from oscar_rosetta import urls as rosetta_urls

  urlpatterns += patterns('',
      ('^dashboard/rosetta/', include(rosetta_urls)),
  )

