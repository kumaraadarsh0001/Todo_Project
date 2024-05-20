from django.db import models

# Create your models here.
STATUS_CHOICES = [
    ('ON', 'ON'),
    ('DONE', 'DONE'),
]


class Todos(models.Model):
    image = models.ImageField(upload_to="todos")
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(choices=STATUS_CHOICES,
                              default="ON", max_length=4)
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
