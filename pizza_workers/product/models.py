from django.db import models


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField(default=1)
    doc = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        pass
