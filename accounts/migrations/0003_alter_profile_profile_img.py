# Generated by Django 3.2.9 on 2022-09-23 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20220815_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_img',
            field=models.ImageField(default='../static/images/avater.png', upload_to=''),
        ),
    ]