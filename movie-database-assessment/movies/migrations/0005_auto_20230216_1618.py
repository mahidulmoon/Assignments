# Generated by Django 3.1.8 on 2023-02-16 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20230216_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
