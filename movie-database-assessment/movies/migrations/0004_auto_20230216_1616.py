# Generated by Django 3.1.8 on 2023-02-16 16:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20230216_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='score',
            field=models.DecimalField(decimal_places=1, max_digits=2, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
