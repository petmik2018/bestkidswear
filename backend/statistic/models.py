from django.db import models

from product.models import Brand, Product
from shops.models import Shop


class AbstractClick(models.Model):
    brand = models.ForeignKey(Brand, related_name='clicks', on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, related_name='clicks', on_delete=models.CASCADE, blank=True, null=True)
    shop = models.ForeignKey(Shop, related_name='clicks', on_delete=models.CASCADE, blank=True, null=True)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.brand:
            return (f"{self.id} {self.brand} {self.date_time.strftime('%d.%m.%Y %H:%M')}")
        if self.product:
            return (f"{self.id} {self.get_product_name()} {self.date_time.strftime('%d.%m.%Y %H:%M')}")
        if self.shop:
            return (f"{self.id} {self.shop} {self.date_time.strftime('%d.%m.%Y %H:%M')}")

    def get_date_time(self):
        return (f"{self.date_time.strftime('%d.%m.%Y %H:%M')}")

    def get_brand_name(self):
        if self.brand:
            return self.brand.name
        else:
            return None

    def get_product_name(self):
        if self.product:
            return self.product.get_fullname()
        else:
            return None

    def get_shop_name(self):
        if self.shop:
            return self.shop.name
        else:
            return None

