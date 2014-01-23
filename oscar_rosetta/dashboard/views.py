from rosetta import views

from django.views.generic import View
from django.http import HttpResponse


class IndexView(View):

    def get(self, request, *args, **kwargs):
        return_value = views.home(request)
        return return_value

    def post(self, request, *args, **kwargs):
        return_value = views.home(request)
        return return_value


class LanguageSelectView(View):

    def get(self, request, *args, **kwargs):
        return_value = views.lang_sel(request, *args, **kwargs)
        return return_value


class LanguagePickView(View):

    def get(self, request, *args, **kwargs):
        return_value = views.list_languages(request, *args, **kwargs)
        return return_value
