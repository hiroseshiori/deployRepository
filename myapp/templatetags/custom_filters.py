# myapp/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter
def times(number, times):
    return range(times)

@register.filter
def sub(value, arg):
    return value - arg
