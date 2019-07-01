from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

#replace .0 by space
@register.filter
def pointzero(value):
    return value.replace(".0","")

