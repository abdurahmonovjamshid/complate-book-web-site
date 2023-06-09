# Generated by Django 4.2 on 2023-04-14 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Categories')),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='img')),
                ('author', models.CharField(max_length=50)),
                ('summary', models.TextField()),
                ('pdf', models.FileField(upload_to='pdf')),
                ('recomended_books', models.BooleanField(default=False)),
                ('fiction_books', models.BooleanField(default=False)),
                ('business_books', models.BooleanField(default=False)),
                ('category', models.ManyToManyField(related_name='books', to='bookapp.category')),
            ],
        ),
    ]
