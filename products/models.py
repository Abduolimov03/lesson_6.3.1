from django.db import models

class Mobile(models.Model):
    model = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    description = models.CharField(default='No Description')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.model}, {self.brand}, {self.description}, {self.price}"