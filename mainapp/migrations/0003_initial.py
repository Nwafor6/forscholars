# Generated by Django 3.2.9 on 2022-08-15 08:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0002_auto_20220815_0938'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('product_price', models.PositiveIntegerField()),
                ('product_cover_image', models.ImageField(upload_to='product-images')),
                ('description', models.CharField(max_length=300)),
                ('status', models.CharField(choices=[('verified', 'verified'), ('pending', 'pending'), ('rejected', 'rejected')], default='pending', max_length=50)),
                ('product_quantity', models.PositiveIntegerField()),
                ('product_location', models.CharField(max_length=100)),
                ('contact', models.CharField(blank=True, max_length=60, null=True)),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
                ('clicks', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('body', models.TextField()),
                ('blog_img', models.ImageField(blank=True, null=True, upload_to='')),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-date_posted',),
            },
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_no', models.CharField(max_length=50)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Product Categories',
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField()),
                ('logo', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('cover_img', models.ImageField(blank=True, null=True, upload_to='')),
                ('faculty', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('school', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.school')),
            ],
            options={
                'verbose_name_plural': 'Departments',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=400)),
                ('slug', models.SlugField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('blog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.blog')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BookCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('course_code', models.CharField(blank=True, max_length=50, null=True)),
                ('about_book', models.CharField(blank=True, max_length=200, null=True)),
                ('slug', models.SlugField()),
                ('file', models.FileField(upload_to='')),
                ('file_type', models.CharField(choices=[('Texts Books', 'Texts Books'), ('Past Questions', 'Past Questions'), ('Hand Outs', 'Hand Outs')], max_length=20)),
                ('cover_img', models.ImageField(blank=True, null=True, upload_to='')),
                ('semester', models.CharField(choices=[('First', 'First'), ('Second', 'Second')], max_length=20)),
                ('year', models.CharField(choices=[('Year-1', 'Year-1'), ('Year-2', 'Year-2'), ('Year-3', 'Year-3'), ('Year-4', 'Year-4'), ('Year-5', 'Year-5')], max_length=20)),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.department')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'BookCategories',
            },
        ),
        migrations.CreateModel(
            name='AdvertImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='product-images')),
                ('advert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.advert')),
            ],
        ),
        migrations.AddField(
            model_name='advert',
            name='product_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.productcategory'),
        ),
        migrations.AddField(
            model_name='advert',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]