# Generated by Django 3.2.7 on 2021-10-05 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='boards',
            field=models.CharField(choices=[('mag', 'MagnetiC Board'), ('nonmag', 'Non-Magnetic'), ('mark', 'Marker Board'), ('pin', 'Soft Board'), ('easel', 'Easel Board'), ('glass', 'Glass Board')], max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('mag', 'Magnetic'), ('nonmag', 'Non-Magnetic'), ('pin', 'Soft Board'), ('mark', 'Marker Board'), ('mdf', 'MDF Board')], max_length=50),
        ),
    ]
