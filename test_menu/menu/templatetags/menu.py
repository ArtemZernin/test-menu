from django import template
from menu.models import Menu
register = template.Library()


@register.inclusion_tag('includes/menu.html')
def draw_menu(slug):
    menu_list = Menu.objects.filter(slug=slug)
    context = {
        'menu_items': menu_list,
    }
    return context

@register.inclusion_tag('includes/submenu.html')
def draw_submenu(m_item, m_list):
    m_list1 = []
    for item in m_list:
        if m_item == item.parent:
            m_list1.append(item)  
    return {'m_items': m_list1, 'menu_items': m_list}