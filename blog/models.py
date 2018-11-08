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
    isi_val = models.FloatField(blank=True, null=True, validators=[MinValueValidator(0.0, message='Must be a number between 0.0 and 1.0'), MaxValueValidator(1.0, message=None)])
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

class Combinatorics_roster(models.Model):
    student_name = models.CharField(max_length=255)
    student_email = models.EmailField()

'''
class NumberPost(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='float_input')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    float_input = models.FloatField()
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.float_input
'''


#class User_input(models.Model):
#    number = models.FloatField(null=True, blank=True, help_text= 'Enter a number.')