from django import template
from django.utils.dateparse import parse_datetime

register = template.Library()

@register.filter(name='string_to_date')
def string_to_date(value):
    return parse_datetime(value)

