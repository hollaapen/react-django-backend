# Generated by Django 4.2.3 on 2023-09-26 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_rename_industry_customer_industries'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('guardian', models.CharField(max_length=50)),
            ],
        ),
    ]