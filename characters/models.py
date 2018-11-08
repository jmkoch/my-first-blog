
from django.db import models

class Foo(models.Model):
    """A magical creature from Foo dynasty"""
    mighty_name = models.CharField(max_length=255)
    kingdoms_count = models.PositiveIntegerField(default=0)
    email = models.EmailField()