# Generated by Django 3.2.3 on 2021-06-23 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='image',
            field=models.ImageField(default='', upload_to='images/'),
        ),
    ]
