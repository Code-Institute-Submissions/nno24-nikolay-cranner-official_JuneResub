# Generated by Django 4.0.4 on 2022-06-28 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_usermessage_newsletter_signup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermessage',
            name='newsletter_signup',
            field=models.BooleanField(default=False),
        ),
    ]
