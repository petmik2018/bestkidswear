# Generated by Django 3.2 on 2021-09-15 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_action_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='detailed_info',
            field=models.TextField(blank=True, null=True),
        ),
    ]
