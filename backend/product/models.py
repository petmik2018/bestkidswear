from django.db import models
from django.conf import settings


class Brand(models.Model):
    name = models.CharField(max_length=64)
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

    def get_brand_url(self):
        curr_brand = f'/{self.slug}/'
        return '/brands' + curr_brand


class Category(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField()

    def __str__(self):
        return self.name


class Product(models.Model):
    brand = models.ForeignKey(Brand, related_name='products', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.PROTECT, blank=True, null=True)
    name = models.CharField(max_length=64)
    color = models.CharField(max_length=64)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    basic_price = models.PositiveIntegerField(blank=True, null=True)
    sizes_scale = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)
    alt = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        unique_together = ('name', 'color')
        ordering = ('-date_added',)

    def __str__(self):
        return self.name + ' ' + self.color

    def get_fullname(self):
        return f'{self.category.name} {self.name} цвет {self.color}'

    def get_absolute_url(self):
        return f'/{self.slug}/'


class ImageLibrary(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Image(models.Model):
    product = models.ForeignKey(Product, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    is_main = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.image)

    def get_image(self):
        if self.image:
            return settings.BASE_URL + self.image.url
        return ''


class ImageSetLoading(models.Model):
    name = models.CharField(max_length=64)
    library = models.ForeignKey(ImageLibrary, on_delete=models.CASCADE)
    loaded_at = models.DateTimeField(auto_now_add=True)
    source = models.FileField(upload_to="uploads/")
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ProductSetLoading(models.Model):
    name = models.CharField(max_length=64)
    loaded_at = models.DateTimeField(auto_now_add=True)
    images_library = models.ForeignKey(ImageLibrary, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)
    source = models.FileField(upload_to="uploads/")
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

