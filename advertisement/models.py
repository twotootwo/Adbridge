from django.db import models

# Create your models here.
class Advertisement(models.Model):
    thumbnail = models.ImageField(upload_to='advertisement/', default='product.svg')
    title = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    description = models.TextField(default='description of the product')
    min_budget = models.PositiveIntegerField(default=0)
    max_budget = models.PositiveIntegerField(default=0)
    detail_1 = models.ImageField(upload_to='advertisement/', default='product.svg')
    detail_2 = models.ImageField(upload_to='advertisement/', default='product.svg')

    def __str__(self):
        return self.name
