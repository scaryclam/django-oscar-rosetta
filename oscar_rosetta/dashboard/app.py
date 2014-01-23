from rosetta import urls

from django.conf.urls import patterns, url

from oscar.core.application import Application

from oscar_rosetta.dashboard import views


class OscarRosettaApplication(Application):

    index_view = views.IndexView

    def get_urls(self):
        urlpatterns = patterns('',
            url(r'^$', self.index_view.as_view(), name="rosetta-index-view"),
        )
        return urlpatterns


application = OscarRosettaApplication()
