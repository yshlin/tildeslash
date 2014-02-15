from django import template
from django.contrib.admin.templatetags.admin_modify import submit_row

register = template.Library()


@register.inclusion_tag('admin/custom_post_submit_line.html', takes_context=True)
def custom_post_submit_row(context):
    return submit_row(context)
