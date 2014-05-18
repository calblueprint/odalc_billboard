from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """Allow dictionary lookups with a variable as the key in templates.

    Usage in templates:
    {% load search_extras %}
    {{ mydict|get_item:var_name }}

    This is equivalent to doing mydict[var_name] in Python.
    """

    return dictionary.get(key)

@register.filter
def get_session(dictionary, key):
    """ Same as above, but converts the key to a string first
    """

    return dictionary.get(str(key))
