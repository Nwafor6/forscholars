# Generated by Django 3.2.9 on 2022-08-10 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_alter_department_faculty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookcategory',
            name='year',
            field=models.CharField(choices=[('Year-1', 'Year-1'), ('Year-2', 'Year-2'), ('Year-3', 'Year-3'), ('Year-4', 'Year-4'), ('Year-5', 'Year-5')], max_length=20),
        ),
        migrations.AlterField(
            model_name='department',
            name='faculty',
            field=models.CharField(max_length=50),
        ),
    ]