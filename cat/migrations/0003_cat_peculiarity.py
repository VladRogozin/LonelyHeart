# Generated by Django 4.2.1 on 2023-07-15 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cat', '0002_cat_tactility'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='peculiarity',
            field=models.CharField(default='не визначено', max_length=100),
        ),
    ]