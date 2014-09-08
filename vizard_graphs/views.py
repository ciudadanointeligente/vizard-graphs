from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse
from vizard_graphs.models import Graph
import json
from django.http import HttpResponse

# Create your views here.

class GraphDisplayView(DetailView):
    model = Graph
    template_name = 'vizard_graphs/single-graph.html'

class GraphUpdateView(UpdateView):
    model = Graph
    fields = ['data']
    content_type = 'application/json'

    def form_valid(self, form):
    	self.object = form.save()
    	return self.render_to_response(form.cleaned_data)

    def render_to_response(self, context, **response_kwargs):
    	data = json.dumps(context)
    	return HttpResponse(data)
