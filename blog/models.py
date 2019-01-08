from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    n_floatNum = models.FloatField(blank=True, null=True)
    n_smallIntNum = models. PositiveSmallIntegerField(blank=True, null=True)
    n_boolVal = models.BooleanField(default=False)
    isi_val = models.FloatField(blank=True, null=True, validators=([MinValueValidator(0.0, message='Must be a number between 0.0 and 1.0'), MaxValueValidator(1.0, message=None)]))
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


class Foo(models.Model):
    mighty_name = models.CharField(max_length=255)
    kingdoms_count = models.PositiveIntegerField(default=0)
    email = models.EmailField()

class Person(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    birth_date = models.DateField()
    location = models.CharField(max_length=100, blank=True)
