# Generated by Django 4.2.3 on 2023-09-20 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='industry',
            new_name='industries',
        ),
    ]
