# Generated by Django 4.0.4 on 2022-05-19 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_bag_bag_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='bag',
            name='bag_quantity',
            field=models.IntegerField(default=0),
        ),
    ]
