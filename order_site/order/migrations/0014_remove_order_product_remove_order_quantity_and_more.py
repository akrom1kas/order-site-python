# Generated by Django 4.0.4 on 2022-04-12 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0013_remove_productorder_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.AddField(
            model_name='order',
            name='Customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.customer'),
        ),
    ]