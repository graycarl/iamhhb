from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def active_for(context, key, name):
    current = getattr(context['request'].resolver_match, key + '_name')
    if name == current:
        return ' active'
    else:
        return ''
