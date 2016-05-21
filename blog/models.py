#see http://tutorial.djangogirls.org/en/django_models/
#for notes


#All lines starting with from or import are
# lines that add some bits from other files.
# So instead of copying and pasting the same
# things in every file, we can include some 
#parts with from ... import ....

from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

#Double-check that you use two underscore 
#characters (_) on each side of str. This 
#convention is used frequently in Python 
#and sometimes we also call them "dunder" 
#(short for "double-underscore").
    def __str__(self):
        return self.title
