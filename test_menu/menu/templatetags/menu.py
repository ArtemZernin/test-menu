from django import template
from menu.models import Menu
register = template.Library()


@register.inclusion_tag('includes/menu.html')
def draw_menu(slug):
    menu_list = Menu.objects.filter(parent=None)
    context = {
        'menu_item': menu_list,
    }
    return context
