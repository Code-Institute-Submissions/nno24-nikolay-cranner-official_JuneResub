# Generated by Django 4.0.4 on 2022-05-19 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.AddField(
            model_name='bag',
            name='bag_items',
            field=models.CharField(blank=True, default='', max_length=254),
        ),
    ]