# Generated by Django 3.0.2 on 2020-01-12 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minimum', '0003_auto_20200112_1609'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Grade',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
    ]
