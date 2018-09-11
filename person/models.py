from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=120, blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="posts")
    def __str__(self):
        return self.name

