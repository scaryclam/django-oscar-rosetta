from rosetta import views

from django.views.generic import TemplateView
from django.http import HttpResponse


class IndexView(TemplateView):
    template_name = 'rosetta/dashboard/index.html'

    def get(self, request, *args, **kwargs):
        super(IndexView, self).get(request, *args, **kwargs)
        return_value = views.home(request)

        return return_value

    def post(self, request, *args, **kwargs):
        return_value = views.home(request)

        return return_value


class LanguageSelectView(TemplateView):
    template_name = 'rosetta/dashboard/index.html'

    def get(self, request, *args, **kwargs):
        super(LanguageSelectView, self).get(request, *args, **kwargs)
        return_value = views.lang_sel(request, *args, **kwargs)
        return return_value


class LanguagePickView(TemplateView):
    template_name = 'rosetta/dashboard/index.html'

    def get(self, request, *args, **kwargs):
        super(LanguagePickView, self).get(request, *args, **kwargs)
        return_value = views.list_languages(request, *args, **kwargs)
        return return_value
