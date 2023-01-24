from django import template
from menu.models import Menu

register = template.Library()

@register.simple_tag()
def draw_menu(name):
    if name == 'all':
        name = ''
    data: dict = \
        Menu.objects.get_menu_and_submenu_items(name)
    return data