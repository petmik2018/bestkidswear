# Generated by Django 3.2 on 2021-05-07 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_rename_main_image_action_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('slug', models.SlugField()),
            ],
        ),
    ]
