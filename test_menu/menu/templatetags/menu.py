from django import template

from menu.models import Menu

register = template.Library()


@register.inclusion_tag('includes/menu.html', takes_context=True)
def draw_menu(context, name):
    menu_list = Menu.objects.filter(name_menu=name)
    temp_path = context['request'].path
    list_tree = []
    for menu_item in menu_list:
        if ('/' + menu_item.slug + '/') == temp_path:
            activ_item = menu_item
            while activ_item.parent is not None:
                list_tree.append(activ_item)
                activ_item = activ_item.parent
            break
    return {'menu_items': menu_list,
            'request': context['request'],
            'list_tree': list_tree}


@register.inclusion_tag('includes/submenu.html', takes_context=True)
def draw_submenu(context, m_item, m_list, list_tree):
    m_list1 = []

    if m_item in list_tree or m_item.parent is None:
        for item in m_list:
            if item.parent == m_item:
                m_list1.append(item)

    return {'m_items': m_list1,
            'menu_items': m_list,
            'request': context['request'],
            'list_tree': list_tree}
