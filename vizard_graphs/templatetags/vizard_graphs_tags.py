from django.template import Library
from django.core.serializers.json import DjangoJSONEncoder
from django.utils.safestring import mark_safe
import json

register = Library()

@register.filter
def data_to_json(graph):
	return mark_safe(json.dumps(graph.data, cls=DjangoJSONEncoder))