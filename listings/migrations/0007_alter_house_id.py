# Generated by Django 4.2.10 on 2024-02-28 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0006_house_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
