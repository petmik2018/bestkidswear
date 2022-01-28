from django.db import models
from django.conf import settings

from product.models import Brand

class Type(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'


class Action(models.Model):
    type = models.ForeignKey(Type, related_name="actions", on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=64)
    slug = models.SlugField()
    image = models.ImageField(upload_to="brands")
    short_info = models.CharField(max_length=255)
    is_active = models.BooleanField(blank=True, null=True)
    brand = models.ForeignKey(Brand, related_name='brand_actions', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'

    def get_image(self):
        if self.image:
            return settings.BASE_URL + self.image.url
        return ''

    def get_brand_url(self):
        curr_brand = f'/{self.brand.slug}/'
        return '/brands' + curr_brand
