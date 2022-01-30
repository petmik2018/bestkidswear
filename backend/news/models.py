from django.db import models
from django.conf import settings


class New(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField()
    main_image = models.ImageField(upload_to="brands")
    short_info = models.CharField(max_length=255)
    detailed_info = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'

    def get_image(self):
        if self.main_image:
            return settings.BASE_URL + self.main_image.url
        return ''
