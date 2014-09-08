from django.test import TestCase
from vizard_graphs.models import Graph
from django.core.urlresolvers import reverse
from django.test.client import Client
from django.template import Template, Context
import json

# Create your tests here.
class GraphModelTestCase(TestCase):
    def setUp(self):
        pass

    def test_instanciate_graph(self):
        '''Instanciate and saving a graph'''
        json_content = '{"anything": "yes anything"}'
        graph = Graph.objects.create(data=json_content)
        self.assertTrue(graph)
        self.assertEquals(graph.data, json_content)


class GraphViewTestCase(TestCase):
    def setUp(self):
        pass

    def test_single_graph_view(self):
        '''There is a view to display a single graph'''
        json_content = '{"anything": "yes anything"}'
        graph = Graph.objects.create(data=json_content)
        url = reverse('single-graph-view', kwargs={'pk':graph.id })
        self.assertTrue(url)
        client = Client()
        response = client.get(url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'vizard_graphs/single-graph.html')
        self.assertTemplateUsed(response, 'vizard_graphs/graph-itself.html')

class GraphUpdateViewTestCase(TestCase):
    def setUp(self):
        pass

    def test_update_graph(self):
        '''A user can udpate the view'''
        json_content = '{"anything": "yes anything"}'
        graph = Graph.objects.create(data=json_content)
        url = reverse('graph-update-view', kwargs={'pk': graph.id})
        self.assertTrue(url)
        c = Client()
        new_data = {'data':'{"anything": "I am refering to a new anything"}'}
        response = c.post(url, data=new_data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.content, json.dumps({'data':
            {u"anything": u"I am refering to a new anything"}
            }))
        updated_graph = Graph.objects.get(id=graph.id)
        self.assertEquals(updated_graph.data, json.loads(new_data['data']))


class GraphJsonViewTemplateTagsTestCase(TestCase):
    '''
    I know that this isn't a very descriptive name but the thing is that this test case 
    aims to test the template tags
    '''
    def setUp(self):
        json_content = '{"anything": "yes anything"}'
        self.graph = Graph.objects.create(data=json_content)

    def test_graph_json_data(self):
        template = Template("{% load vizard_graphs_tags %}{{ graph|data_to_json }}")
        context = Context({
            'graph': self.graph
        })
        self.assertEqual(template.render(context), u'"{\\"anything\\": \\"yes anything\\"}"')
