# Generated by Django 3.2 on 2021-08-09 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
