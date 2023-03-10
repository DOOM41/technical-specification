# Django
from django.core.handlers.wsgi import WSGIRequest
from django.views import View
from django.template import loader
from django.http import HttpResponse, Http404
from django.template import Template

# APPS
from menu.models import Menu


class MenuView(View):
    template_name: str = 'menu.html'

    def get(self, request: WSGIRequest):
        template: Template = loader.get_template(
            self.template_name
        )
        return HttpResponse(
            template.render(
                request=request,
            ),
            content_type='text/html'
        )
