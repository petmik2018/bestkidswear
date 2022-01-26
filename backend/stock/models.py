from django.db import models

from product.models import Product


class Stock(models.Model):
    product = models.ForeignKey(Product, related_name="stocks", on_delete=models.CASCADE, blank=True, null=True)
    size = models.CharField(max_length=64)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        ordering = ('product', 'size',)

    def __str__(self):
        return f'{self.product.slug} размер {self.size}'


class StockSetLoading(models.Model):
    name = models.CharField(max_length=64)
    loaded_at = models.DateTimeField(auto_now_add=True)
    source = models.FileField(upload_to="uploads/")
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
