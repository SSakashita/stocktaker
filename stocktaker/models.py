from django.conf import settings
from django.db import models
from django.utils import timezone


class Item(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    category = models.CharField(max_length=10)
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField(default=100)
    note = models.CharField(max_length=20, blank=True)
    stocked_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name