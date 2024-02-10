from django.db import models

class FAQ(models.Model):
    FAQ_CATEGORY_CHOICES = [
        ('PRODUCTS', 'Products'),
        ('ORDERS_DELIVERY', 'Orders and Delivery'),
        ('CONTACT_US', 'Contact Us'),
    ]

    question = models.CharField(max_length=255)
    answer = models.TextField()
    category = models.CharField(max_length=20, choices=FAQ_CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)  # Importing and using DateTimeField
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question

