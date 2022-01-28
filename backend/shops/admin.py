from django.contrib import admin
from pyexcel_xlsx import get_data

from .models import Shop, ShopBrand
from .models import WhereToBuy, WhereToBuyUpload
from product.models import Product


class WhereToBuyUploadAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'loaded_at', 'completed')
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
                    my_loading = loading
                    data = get_data(file_name)
                    collection = data.get("Sheet1")
                    collection.pop(0)
                    for item in collection:
                        my_slug = f'{item[0]}_{item[1]}'
                        if len(item) == 4:
                            my_product = Product.objects.get(slug=my_slug)
                            WhereToBuy.objects.create(product=my_product, shop=item[2], link=item[3])

                        message_bit = "Информация загружена в базу"
        else:
            message_bit = "Из соображений безопасности закачка файдов разшена по одному"
        self.message_user(request, f'{message_bit}')


admin.site.register(Shop)
admin.site.register(ShopBrand)
admin.site.register(WhereToBuy)
admin.site.register(WhereToBuyUpload, WhereToBuyUploadAdmin)
