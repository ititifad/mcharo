# Generated by Django 4.2.1 on 2024-05-25 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='service/images/')),
            ],
        ),
    ]
