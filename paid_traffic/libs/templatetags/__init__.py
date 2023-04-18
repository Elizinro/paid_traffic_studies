from django import template
from django.contrib.auth.models import Group
import datetime as dt
import logging

register = template.Library()

# Get attribute
@register.simple_tag
def get_attribute(obj, attribute):
    return getattr(obj, attribute)

# Retorna True ou False dependendo se o user está ou não dentro do grupo
@register.filter(name='in_group')
def in_group(user: object, group_name: str):
    return user.groups.filter(name=group_name).exists()

# Tradução das colunas, TODO fazer uma forma em que isso fique em uma classe ou de forma mais organizada
FIELDS_TRANSLATION = {}
main_fields_translations = {
    "id": "Id",
}
FIELDS_TRANSLATION.update(main_fields_translations)