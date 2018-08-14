from django import template

register = template.Library()

@register.filter(name='cut')
def dummy_filter(value, arg):

    """
    basically doing a cut
    """

    return value.replace(arg,"")


# (name of filter, actual function to call)
#
# register.filter('cut', dummy_filter)
