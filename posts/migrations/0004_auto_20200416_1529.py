# Generated by Django 3.0.5 on 2020-04-16 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20200416_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedsmodel',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/fricle/image/'),
        ),
    ]