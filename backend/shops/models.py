from django.db import models
from django.conf import settings


class Shop(models.Model):
    CHOICES = (
        ('Off line', 'Off line'),
        ('On line', 'On line'),
        ('Mixed', 'Mixed')
    )
    name = models.CharField(max_length=64)
    type = models.CharField(max_length=16, choices=CHOICES)
    slug = models.SlugField()
    logo_image = models.ImageField(upload_to="brands")
    main_image = models.ImageField(upload_to="brands")
    short_info = models.CharField(max_length=255)
    detailed_info = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'

    def get_logo(self):
        if self.logo_image:
            return settings.BASE_URL + self.logo_image.url
        return ''

    def get_image(self):
        if self.main_image:
            return settings.BASE_URL + self.main_image.url
        return ''

    def get_shop_url(self):
        curr_shop = f'/{self.slug}/'
        return '/shops' + curr_shop
