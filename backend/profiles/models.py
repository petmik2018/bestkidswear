from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

INITIAL_BONUSES = [
    (100, '100'),
    (200, '200'),
    (300, '300'),
]

User = get_user_model()


class BonusSettings(models.Model):
    initial_bonus = models.PositiveIntegerField(unique=True, choices=INITIAL_BONUSES, verbose_name='Initial bonus')

    class Meta:
        verbose_name = 'bonus settings'
        verbose_name_plural = 'bonus settings'

    def __str__(self):
        return dict(INITIAL_BONUSES).get(self.initial_bonus, self.initial_bonus)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=16, blank=True, null=True)
    email = models.CharField(max_length=16, blank=True, null=True)
    phone = models.CharField(max_length=16, blank=True, null=True)
    address = models.CharField(max_length=256)
    parent = models.ForeignKey(User, related_name='children', on_delete=models.CASCADE, blank=True, null=True)
    bonuses = models.PositiveIntegerField(blank=True, null=True)
    is_shop_owner = models.BooleanField(default=False)
    is_brand_owner = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def get_user_id(self):
        return self.user.id

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, email=instance.email)
    instance.profile.save()

