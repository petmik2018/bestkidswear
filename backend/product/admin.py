from django.contrib import admin
from django.conf import settings
from pyexcel_xlsx import get_data

from .models import Brand, Category, Product, ImageLibrary, Image, ImageSetLoading, ProductSetLoading
from stock.models import Stock

import os
import zipfile


class ProductSetLoadingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'loaded_at', 'images_library', 'completed')
    actions = ["complete_loading"]
    list_editable = ['completed']

    def complete_loading(self, request, queryset):
        row_update = queryset.count()
        if row_update == 1:
            for loading in queryset:
                if loading.completed:
                   message_bit = "Информация загрузки уже в базе"
                else:
                    queryset.update(completed=True)
                    file_name = loading.source
                    data = get_data(file_name)
                    collection = data.get("Sheet1")
                    collection.pop(0)

                    my_im_lib = loading.images_library.name
                    # my_action = loading.action

                    for item in collection:
                        my_brand = Brand.objects.get(name=item[2])
                        my_slug = f'{item[0]}_{item[1]}'
                        my_category = Category.objects.get(name=item[3])
                        my_product = Product.objects.create(name=item[0], color=item[1],
                                                            slug=my_slug, brand=my_brand,
                                                            category=my_category, description=item[4],
                                                            basic_price=item[5], sizes_scale=item[6], alt=item[8])
                        stocks = item[6].split(" ")
                        for stock in stocks:
                            stock.strip()
                            if stock != '':
                                Stock.objects.create(product=my_product, size=stock, price=item[5], quantity=0)
                        images = item[7].split(" ")
                        item_is_main = 1
                        for image in images:
                            image.strip()
                            if image != '':
                                Image.objects.create(product=my_product, image="products/"+my_im_lib+"/"+image,
                                                     is_main=item_is_main)
                                item_is_main = 0
                        message_bit = "Информация загружена в базу"
        else:
            message_bit = "Из соображений безопасности закачка файдов разшена по одному"
        self.message_user(request, f'{message_bit}')


class ImageSetLoadingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'library', 'loaded_at', 'source', 'completed')
    actions = ["complete_loading"]
    list_editable = ['completed']

    def complete_loading(self, request, queryset):
        row_update = queryset.count()
        if row_update == 1:
            for loading in queryset:
                if loading.completed:
                    message_bit = "Изображения уже загружены"
                else:
                    queryset.update(completed=True)
                    zip_file_name = os.path.join(settings.MEDIA_ROOT, loading.source.name)
                    target_path = os.path.join(settings.MEDIA_ROOT, "products",  loading.library.name)
                    with zipfile.ZipFile(zip_file_name, "r") as zip_ref:
                        zip_ref.extractall(target_path)
                    message_bit = "Распаковка из " + zip_file_name + " в " + target_path
        else:
            message_bit = "Из соображений безопасности закачка изображений ограничена одним архивом"

        self.message_user(request, f'{message_bit}')


admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ImageLibrary)
admin.site.register(Image)
admin.site.register(ImageSetLoading, ImageSetLoadingAdmin)
admin.site.register(ProductSetLoading, ProductSetLoadingAdmin)
