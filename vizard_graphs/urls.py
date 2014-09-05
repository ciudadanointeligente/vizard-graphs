from django.conf.urls import url

from vizard_graphs.views import GraphDisplayView, GraphUpdateView

urlpatterns = [
    url(r'^graphs/(?P<pk>\d+)/?$', GraphDisplayView.as_view(), name='single-graph-view'),
    url(r'^graphs/(?P<pk>\d+)/update/?$', GraphUpdateView.as_view(), name='graph-update-view')

]

