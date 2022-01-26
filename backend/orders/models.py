from django.db import models
from profiles.models import User


class Order(models.Model):
    CREATED = 'Создан'
    PREPARED = 'Собран'
    ONTHEWAY = 'В пути'
    COMPLETED = 'Доставлен'
    CANCELLED = 'Отменен'
    ORDER_STATUS = [
        (CREATED, 'Создан'),
        (PREPARED, 'Собран'),
        (ONTHEWAY, 'В пути'),
        (COMPLETED, 'Доставлен'),
        (CANCELLED, 'Отменен'),
    ]
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    status = models.CharField(max_length=64, choices=ORDER_STATUS, default=CREATED)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f"{self.id} {self.user.username} {self.date_added.strftime('%d.%m.%Y %H:%M')} {self.status}")

    def get_user_name(self):
        return self.user.username

    def get_data(self):
        return (f"{self.date_added.strftime('%d.%m.%Y %H:%M')}")


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product_id = models.PositiveIntegerField(blank=True, null=True)
    product = models.CharField(max_length=128)
    size = models.CharField(max_length=16)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return (f"{self.order.id} {self.product} размер {self.size}")
