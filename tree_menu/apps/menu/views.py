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

    def get(self, request: WSGIRequest, menu_name):
        template: Template = loader.get_template(
            self.template_name
        )
        # for all data
        if menu_name == 'all':
            menu_name = ''
        data: dict = \
            Menu.objects.get_menu_and_submenu_items(menu_name)
        if not data:
            raise Http404
        return HttpResponse(
            template.render(
                context={'data': data},
                request=request,
            ),
            content_type='text/html'
        )
