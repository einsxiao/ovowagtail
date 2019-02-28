from django import template
register = template.Library()

@register.filter
def get_type(value):
    return type(value)

# safe filter should use here to avoid escape char like '<'...
# @register.filter
# def help_text_filter(text):
#     return text.replace("&lt;/li&gt;&lt;li&gt;","</li><li>").replace("&lt;ul&gt;&lt;li&gt;","<ul><li>").replace("&lt;/li&gt;&lt;/ul&gt;","</li></ul>")
