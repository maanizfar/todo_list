from django.db import models
from django.contrib.auth import get_user_model


class Task(models.Model):
    text = models.TextField(blank=False, null=False, max_length=200)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
