# Generated by Django 3.1.5 on 2021-02-02 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20210128_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='rate',
            field=models.DecimalField(decimal_places=1, max_digits=2, verbose_name='Rate'),
        ),
    ]
