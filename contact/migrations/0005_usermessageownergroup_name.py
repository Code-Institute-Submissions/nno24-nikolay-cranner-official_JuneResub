# Generated by Django 4.0.4 on 2022-06-28 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_usermessageowner_usermessageownergroup'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermessageownergroup',
            name='name',
            field=models.CharField(default='self', max_length=30),
        ),
    ]
