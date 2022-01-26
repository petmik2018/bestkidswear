from django.contrib import admin

from pyexcel_xlsx import get_data

from .models import Stock, StockSetLoading
from product.models import Product


class StockSetLoadingAdmin(admin.ModelAdmin):
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
                    data = get_data(file_name)
                    collection = data.get("Sheet1")
                    collection.pop(0)

                    for item in collection:
                        my_product = Product.objects.filter(name=item[0]).get(color=item[1])
                        my_stock = my_product.stocks.all().get(size=item[2])
                        my_stock.quantity = int(item[3])
                        my_stock.price = int(item[4])
                        my_stock.save()

                        message_bit = "Информация о количествах и ценах загружена в базу"
        else:
            message_bit = "Из соображений безопасности закачка файлов разшена по одному"
        self.message_user(request, f'{message_bit}')


admin.site.register(Stock)
admin.site.register(StockSetLoading, StockSetLoadingAdmin)
