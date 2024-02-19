from django import template

register = template.Library()

@register.simple_tag
def make_stars(rating):
    return '★' * int(rating) + '☆' * (5 - int(rating))
