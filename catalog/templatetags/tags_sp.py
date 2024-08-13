from django import template

register = template.Library()


@register.filter()
def len_char_filter(description):
    if len(description) > 10:
        return description[0:10]

    return description
