# Generated by Django 4.2.1 on 2024-05-23 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('original_image', models.ImageField(upload_to='gallery/originals/')),
                ('thumbnail_image', models.ImageField(upload_to='gallery/thumbnails/')),
            ],
        ),
    ]