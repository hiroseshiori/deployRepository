from django import template

register = template.Library()

@register.filter(name='range')
def filter_range(number):
    return range(number)
