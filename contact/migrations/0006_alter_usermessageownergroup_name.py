# Generated by Django 4.0.4 on 2022-06-28 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_usermessageownergroup_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermessageownergroup',
            name='name',
            field=models.CharField(choices=[('Booking', 'Booking'), ('Other', 'Other')], default='Booking', max_length=15),
        ),
    ]