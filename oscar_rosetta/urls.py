from rosetta import urls as rosetta_urls

from django.conf.urls import patterns, url

from oscar_rosetta.dashboard import views


rosetta_patterns = rosetta_urls.urlpatterns


map_classes = {
    'rosetta-home': views.IndexView.as_view(),
    'rosetta-language-selection': views.LanguageSelectView.as_view(),
    'rosetta-pick-file': views.LanguagePickView.as_view(),
}


patched_patterns = []
for url_pattern in rosetta_patterns:
    view = map_classes.get(url_pattern.name, views.IndexView.as_view())
    patched_patterns.append(
        url(url_pattern.regex.pattern, view, name=url_pattern.name))


urlpatterns = patterns('', *patched_patterns)
