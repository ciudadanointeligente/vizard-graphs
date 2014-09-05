from django.db import models
from jsonfield import JSONField
# Create your models here.

class Graph(models.Model):
    data = JSONField()
