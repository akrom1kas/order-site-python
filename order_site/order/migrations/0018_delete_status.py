# Generated by Django 4.0.4 on 2022-04-12 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0017_remove_order_status_order_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Status',
        ),
    ]