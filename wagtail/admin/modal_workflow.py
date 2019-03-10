import json
from django.http import JsonResponse
from django.http import HttpResponse
from django.template.loader import render_to_string


def render_modal_workflow(request, html_template, js_template=None, template_vars=None, json_data=None):
    """"
    Render a response consisting of an HTML chunk and a JS onload chunk
    in the format required by the modal-workflow framework.
    """
    if js_template:
        raise TypeError("Passing a js_template argument to render_modal_workflow is no longer supported")

    # construct response as JSON
    response = {}

    if html_template:
        response['html'] = render_to_string(html_template, template_vars or {}, request=request)

    if json_data:
        response.update(json_data)

    return JsonResponse(response)

# def render_modal_workflow(request, html_template, js_template, template_vars=None):
#     """"
#     Render a response consisting of an HTML chunk and a JS onload chunk
#     in the format required by the modal-workflow framework.
#     """
#     response_keyvars = []

#     if html_template:
#         html = render_to_string(html_template, template_vars or {}, request=request)
#         response_keyvars.append("'html': %s" % json.dumps(html))

#     if js_template:
#         js = render_to_string(js_template, template_vars or {}, request=request)
#         response_keyvars.append("'onload': %s" % js)

#     response_text = "{%s}" % ','.join(response_keyvars)

#     return HttpResponse(response_text, content_type="text/javascript")
