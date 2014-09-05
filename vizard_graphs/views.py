from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse
from vizard_graphs.models import Graph

# Create your views here.

class GraphDisplayView(DetailView):
    model = Graph
    template_name = 'vizard_graphs/single-graph.html'

class GraphUpdateView(UpdateView):
    model = Graph
    fields = ['data']

    def get_success_url(self):
        return reverse('single-graph-view', kwargs={'pk':self.object.id })

