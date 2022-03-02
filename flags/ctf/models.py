from django.db import models


class User(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=60)
    def __str__(self):
        return self.name
