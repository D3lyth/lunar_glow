from django.db import models

class ScentProfile(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name


class ProductScent(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    scentoptions = models.ForeignKey(ScentProfile, on_delete=models.CASCADE, null=True, blank=True)
    products = models.ManyToManyField('products.Product')

    def __str__(self):
        return self.name
