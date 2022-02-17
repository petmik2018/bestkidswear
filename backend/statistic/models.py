from django.db import models

from product.models import Brand


class BrandClick(models.Model):
    brand = models.ForeignKey(Brand, related_name='clicks', on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f"{self.id} {self.brand} {self.date_time.strftime('%d.%m.%Y %H:%M')}")

    def get_date_time(self):
        return (f"{self.date_time.strftime('%d.%m.%Y %H:%M')}")

    def get_brand_name(self):
        return self.brand.name

