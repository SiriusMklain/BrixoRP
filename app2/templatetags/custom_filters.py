# custom_filters.py
from django import template

register = template.Library()


@register.filter(name='dict_lookup')
def dict_lookup(d, key):
    return d.get(key, None)
