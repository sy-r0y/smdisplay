# Generated by Django 3.2.7 on 2021-10-03 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('plate_images', models.ImageField(upload_to='plateimg')),
                ('category', models.CharField(choices=[('c', 'curved'), ('f', 'flat'), ('a', 'aluminum'), ('w', 'wooden')], max_length=20)),
            ],
        ),
    ]