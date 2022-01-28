from django.db import models
from django.conf import settings

from product.models import Brand, Product


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
    main_link = models.CharField(max_length=128, blank=True, null=True)


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


class ShopBrand(models.Model):
    brand = models.ForeignKey(Brand, related_name="shops", on_delete=models.CASCADE, blank=True, null=True)
    shop = models.ForeignKey(Shop, related_name="brands", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.shop.name + "-> " + self.brand.name

    def get_brand_name(self):
        return self.brand.name

    def get_brand_link(self):
        return self.brand.get_absolute_url()


class WhereToBuy(models.Model):
    product = models.ForeignKey(Product, related_name="where_to_buy", on_delete=models.CASCADE)
    shop = models.CharField(max_length=64, null=True, blank=True)
    link = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        my_name = self.product.name + ' ' + self.product.color + ' ' + str(self.id)
        return my_name


class WhereToBuyUpload(models.Model):
    name = models.CharField(max_length=64)
    loaded_at = models.DateTimeField(auto_now_add=True)
    source = models.FileField(upload_to="uploads/")
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
